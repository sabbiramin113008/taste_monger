# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""


def leaderboard_generation_task():
    print('### Starting LeaderBoard Update  ###')
    from datetime import timedelta, datetime

    from menu_app.models import Menu, Leaderboard
    today = datetime.today().date()
    yesterday = datetime.today() - timedelta(days=1)
    day_before_yesterday = datetime.today() - timedelta(days=2)
    query = Menu.objects.filter(c_date=today).order_by('-vote_count')
    for m in query:
        r = m.restaurant
        try:
            l = Leaderboard.objects.filter(restaurant=r, c_date=yesterday.date()).first()
        except Exception as e:
            print('Error Getting yesterday :', e)
            l = None
        try:
            ll = Leaderboard.objects.filter(restaurant=r, c_date=day_before_yesterday.date()).first()
        except Exception as e:
            ll = None
            print('Error Getting yes-1 day:', e)

        if l and ll:
            continue
        try:
            nl = Leaderboard.objects.get(c_date=today)
            nl.restaurant = r
            nl.save()
        except:
            nl = Leaderboard.objects.create(c_date=today, restaurant=r)
            nl.save()
        break
    print('### Ending LeaderBoard Update  ###')
