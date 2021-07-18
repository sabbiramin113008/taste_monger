# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from rest_framework import serializers

from menu_app.models import Restaurant, Item, Menu, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'created']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'ingredients', 'item_type']


class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'name', 'ingredients', 'item_type', 'vote_count']


class VoteSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()

    class Meta:
        model = Vote
        fields = ['id', 'menu', 'hasLiked']
