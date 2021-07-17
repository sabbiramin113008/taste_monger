# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from menu_app.models import Item
from menu_app.serializers import ItemSerializer


class ItemApi(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        response = dict()
        try:
            item = Item.objects.create(
                name=data.get('name'),
                ingredients=data.get('ingredients'),
                item_type=data.get('item_type')
            )
            item.save()
            response['status'] = 'created'
            response['model'] = ItemSerializer(item).data
            return Response(response)

        except Exception as e:
            print('Error Creating Restaurant:', e)
            response['status'] = 'Error'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
