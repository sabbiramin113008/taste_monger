# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from menu_app.models import Restaurant
from menu_app.serializers import RestaurantSerializer


class RestaurantApi(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        response = dict()
        try:
            restaurant = Restaurant.objects.create(name=data.get('name'))
            restaurant.save()
            response['status'] = 'created'
            response['model'] = RestaurantSerializer(restaurant).data
            return Response(response)
        except Exception as e:
            print('Error Creating Restaurant:', e)
            response['status'] = 'Error'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
