# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 17 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
import datetime

from django.utils.timezone import now
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.datetime_safe import date

UserModel = get_user_model()


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(null=False, unique=True, max_length=20)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


food_type = [
    ('DRINK', 'DRINK'),
    ('MEAL', 'MEAL'),
    ('DESERT', 'DESERT'),
    ('MAIN_DISH', 'MAIN_DISH')
]


class Item(models.Model):
    name = models.CharField(null=False, max_length=50)
    ingredients = models.TextField(null=False, default='')
    item_type = models.CharField(null=False, max_length=50, choices=food_type, default='MAIN_DISH')

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='restaurant', null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=50)
    ingredients = models.TextField(null=False, default='')
    item_type = models.CharField(null=False, max_length=50, choices=food_type, default='MAIN_DISH')
    c_date = models.DateField(default=now)  # Todo:// Need to restrict editing any past menuItem
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return '{} from {}'.format(self.name, self.restaurant)


class Vote(models.Model):
    # Todo:// allow user to only vote for current day
    menu = models.ForeignKey(Menu, related_name='menu', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, null=False, related_name='users', on_delete=models.CASCADE)
    hasLiked = models.BooleanField(default=False)

    def __str__(self):
        return '{} - liked - {}'.format(self.user.username, self.menu)


class Leaderboard(models.Model):
    c_date = models.DateField(null=False)
    restaurant = models.ForeignKey(Restaurant, related_name='leaderboardrestaurant', null=False,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant.name
