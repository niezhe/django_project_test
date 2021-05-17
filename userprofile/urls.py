#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： jenny
# datetime： 2021/5/11 9:36 
# File ：urls.py
from django.urls import path
from . import views

# 正在部署的应用名称
app_name = "userprofile"
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.user_register,name='register'),
]
