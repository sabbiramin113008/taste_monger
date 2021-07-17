# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 17 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from django.contrib import admin

# Register your models here.
from menu_app.models import Restaurant, Item, Menu, Vote

admin.site.site_header = 'Taste-Monger'
admin.site.site_title = 'Taste-Monger 1.0'
admin.site.index_title = 'Welcome to Taste-Monger Admin 1.0'

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Vote)
