# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from django.core.management import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model

from menu_app.models import Restaurant, Menu


class Command(BaseCommand):
    def _create_users(self):
        faker = Faker()
        UserModel = get_user_model()
        for i in range(1, 30):
            username = faker.first_name()
            email = faker.email()
            password = '123456'
            print(username, email, password)
            try:
                user = UserModel.objects.create_user(
                    username, email, password
                )
            except Exception as e:
                print('Error Creating Fake User:', e)

    def handle(self, *args, **options):
        self._create_users()
