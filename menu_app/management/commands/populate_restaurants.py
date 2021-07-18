# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""

from django.core.management import BaseCommand

from menu_app.models import Restaurant


class Command(BaseCommand):
    def _create_restaurants(self):
        names = ['Best Meals', 'Masala Indians', 'Gold Kitchen',
                 'Hells Kitchen', 'Best Foods', 'Al Kebabs',
                 'Night Fury', 'Camoe Cuisine'
                 ]
        for k in names:
            try:
                restaurant = Restaurant.objects.create(
                    name=k
                )
                restaurant.save()
            except:
                pass

    def handle(self, *args, **options):
        self._create_restaurants()
