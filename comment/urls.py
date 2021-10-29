#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： jenny
# datetime： 2021/10/28 15:56 
# File ：urls.py
from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]
