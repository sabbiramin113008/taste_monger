"""tastemonger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from menu_app.ApiViews.CustomAuthApi import EmployeeRegister
from menu_app.ApiViews.ItemApi import ItemApi
from menu_app.ApiViews.MenuApi import MenuApi
from menu_app.ApiViews.RestaurantApi import RestaurantApi
from menu_app.ApiViews.VoteApi import VoteApi

urlpatterns = [
    path('admin/', admin.site.urls),
    # Auth APIs
    path('api/v1/auth/register/', EmployeeRegister.as_view(), name='Register'),
    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='Get JWT Token'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='Get JWT Refresh Token'),

    # Restaurant APIs
    path('api/v1/restaurant/', RestaurantApi.as_view(), name='Restaurant APIs'),

    # Items APIs
    path('api/v1/item/', ItemApi.as_view(), name='Items APIs'),

    # Menu APIs
    path('api/v1/menu/', MenuApi.as_view(), name='Menu APIs'),

    # Voting APIs
    path('api/v1/vote/', VoteApi.as_view(), name='Voting APIs'),

]
