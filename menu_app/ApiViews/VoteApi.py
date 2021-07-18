# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
import datetime

from django.db import transaction
from django.core.paginator import Paginator
from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from menu_app.models import Restaurant, Menu, Vote
from menu_app.serializers import RestaurantSerializer, MenuSerializer, VoteSerializer


class VoteApi(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_menu_object(self, pk):
        try:
            return Menu.objects.get(pk=pk)
        except Exception as e:
            raise Http404

    def post(self, request):
        user = request.user
        data = request.data
        today = datetime.datetime.today().date()
        menu = self.get_menu_object(data.get('menu_id'))
        hasLiked = data.get('hasLiked', True)
        print(menu.name)
        if today > menu.c_date:
            return Response(data={'error': 'Can Not Vote for Past Day Menu'},
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if today < menu.c_date:
            return Response(data={'error': 'Can Not Vote for Future Day Menu'},
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if today == menu.c_date:
            with transaction.atomic():
                vote, _ = Vote.objects.get_or_create(
                    menu=menu,
                    user=user
                )
                vote.hasLiked = hasLiked
                vote.save()
                pre_count = menu.vote_count
                if hasLiked:
                    menu.vote_count = pre_count + 1
                else:
                    temp = 0 if pre_count - 1 < 0 else pre_count - 1
                    menu.vote_count = temp
                menu.save()
                response = {
                    'status': 'success',
                    'model': VoteSerializer(vote).data
                }
                return Response(response, status=status.HTTP_200_OK)
        return Response(data={'error': 'Something Went Wrong'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
