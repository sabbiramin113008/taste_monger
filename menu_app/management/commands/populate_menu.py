# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from django.core.management import BaseCommand

from menu_app.models import Restaurant, Menu


class Command(BaseCommand):
    def _create_menu(self):
        names = ['Best Meals', 'Masala Indians', 'Gold Kitchen',
                 'Hells Kitchen', 'Best Foods', 'Al Kebabs',
                 'Night Fury', 'Camoe Cuisine'
                 ]

        items = [
            {
                'name': 'Masala Chicken',
                'ingredients': 'Chicken, Masala, Indian Curd',
                'item_type': 'MAIN_DISH',
            },
            {
                'name': 'Dosa Chicken',
                'ingredients': 'Nun, Chicken, Masala, Indian Curd',
                'item_type': 'MAIN_DISH',
            },
            {
                'name': 'Rice Chicken',
                'ingredients': 'Rice, Chicken, Masala, Indian Curd',
                'item_type': 'MAIN_DISH',
            },
            {
                'name': 'Beef Biriyani',
                'ingredients': 'Beef, Rice, Chutney',
                'item_type': 'MAIN_DISH',
            },
            {
                'name': 'Kabuli Polao',
                'ingredients': 'Beef, Rice, Salad',
                'item_type': 'MAIN_DISH',
            },
            {
                'name': 'Beef Kacchi',
                'ingredients': 'Beef, Basmati Rice, Chutney',
                'item_type': 'MAIN_DISH',
            },
            {
                'name': 'Double Cheese Burger',
                'ingredients': 'Beef , Cheese, Sauce',
                'item_type': 'MAIN_DISH',
            }

        ]
        for name in names:
            r = Restaurant.objects.get(name=name)
            for item in items:
                try:
                    m = Menu.objects.create(
                        restaurant=r,
                        name=item.get('name'),
                        ingredients=item.get('ingredients'),
                        item_type=item.get('item_type')
                    )
                    m.save()
                except Exception as e:
                    print('Error saving Items:', e)

    def handle(self, *args, **options):
        self._create_menu()
