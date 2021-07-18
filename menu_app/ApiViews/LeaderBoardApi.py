# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from datetime import datetime, timedelta

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from menu_app.models import Restaurant, Menu, Leaderboard
from menu_app.serializers import RestaurantSerializer, MenuSerializer


class LeaderBoard(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        today = datetime.today().date()
        yesterday = datetime.today() - timedelta(days=1)
        day_before_yesterday = datetime.today() - timedelta(days=2)
        query = Menu.objects.filter(c_date=today).order_by('-vote_count')
        model = None
        for m in query:
            r = m.restaurant
            try:
                l = Leaderboard.objects.filter(restaurant=r, c_date=yesterday.date()).first()
            except Exception as e:
                l = None
            try:
                ll = Leaderboard.objects.filter(restaurant=r, c_date=day_before_yesterday.date()).first()
            except Exception as e:
                ll = None

            if l and ll:
                continue
            try:
                nl = Leaderboard.objects.get(c_date=today)
                nl.restaurant = r
                nl.save()
            except:
                nl = Leaderboard.objects.create(c_date=today, restaurant=r)
                nl.save()
            model = {
                'id': nl.id,
                'restaurent': RestaurantSerializer(r).data,
                'menu': MenuSerializer(m).data
            }
            break
        response = {
            'model': model
        }
        return Response(response, status.HTTP_200_OK)
