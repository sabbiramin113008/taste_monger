# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from django.core.management import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model

from menu_app.models import Restaurant, Menu, Vote
import random


class Command(BaseCommand):
    def _cast_fake_vote(self):
        selected_menu = [13, 6, 26]
        users = get_user_model().objects.all()
        for user in users:
            print(user.username, random.choice(selected_menu))
            s_menu = random.choice(selected_menu)
            try:
                menu = Menu.objects.get(pk=s_menu)
                v, _ = Vote.objects.get_or_create(
                    menu=menu,
                    user=user
                )
                v.save()
                pre_count = menu.vote_count
                menu.vote_count = pre_count + 1
                menu.save()
            except Exception as e:
                print('Error Casting Fake Votes:', e)

    def handle(self, *args, **options):
        self._cast_fake_vote()
