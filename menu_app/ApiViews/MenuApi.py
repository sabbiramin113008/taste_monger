# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
import datetime

from django.core.paginator import Paginator
from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from menu_app.models import Restaurant, Menu
from menu_app.serializers import RestaurantSerializer, MenuSerializer


class MenuApi(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_restaurant(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Exception as e:
            raise Http404

    def post(self, request):
        data = request.data
        restaurant = self.get_restaurant(data.get('restaurant_id'))
        items = data.get('items')
        response = dict()
        models = list()
        for item in items:
            date_format = '%Y-%m-%d'
            date_string = data.get('date', None)
            today = datetime.datetime.today().date()
            if date_string:
                date_obj = datetime.datetime.strptime(date_string, date_format).date()
                if today > date_obj:
                    return Response(data={'error': 'Can Not Add Menu in Past Dates'},
                                    status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            else:
                date_obj = today

            try:
                menu, _ = Menu.objects.get_or_create(
                    restaurant=restaurant,
                    name=item.get('name'),
                    ingredients=item.get('ingredients'),
                    item_type=item.get('item_type'),
                    c_date=date_obj
                )
                menu.save()
                models.append(MenuSerializer(menu).data)
            except Exception as e:
                response['error'] = 'Error Saving Menu'
                return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        response['status'] = 'success'
        response['models'] = models
        return Response(response)

    def get(self, request):
        date_format = '%Y-%m-%d'
        date_string = self.request.query_params.get('date')

        today = datetime.datetime.today().date()
        if not date_string:
            date_obj = today
        else:
            date_obj = datetime.datetime.strptime(date_string, date_format)

        page_number = self.request.query_params.get('page', 1)
        page_limit = self.request.query_params.get('limit', 30)

        queryset = Menu.objects.filter(c_date=date_obj)
        total_count = queryset.count() if queryset.count() else 0
        paginator = Paginator(queryset, page_limit)
        paginated_objects = paginator.get_page(number=page_number)

        serializer = MenuSerializer(paginated_objects, many=True)
        data = {
            'total_count': total_count,
            'results': serializer.data
        }
        return Response(data=data)
