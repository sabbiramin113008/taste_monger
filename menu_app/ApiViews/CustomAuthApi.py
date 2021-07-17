# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class EmployeeRegister(APIView):
    def post(self, request):
        response = dict()
        data = request.data
        if UserModel.objects.filter(email=data.get('email')).exists():
            response['error'] = 'Email Already Taken'
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        if UserModel.objects.filter(username=data.get('username')).exists():
            response['error'] = 'Username Already Taken'
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        user = UserModel.objects.create_user(data.get('username'), data.get('email'), data.get('password'))
        if user:
            response['success'] = 'Successfully Registered'
            return Response(response)
        else:
            response['error'] = 'Something Went Wrong'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
