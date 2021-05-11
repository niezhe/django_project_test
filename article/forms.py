#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： jenny
# datetime： 2021/5/11 17:26 
# File ：forms.py
from django import forms
# 引入文章模型
from .models import ArticlePost


# 写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型的来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body')
