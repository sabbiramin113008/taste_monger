# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from rest_framework import serializers

from menu_app.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name','created']