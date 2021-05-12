#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： jenny
# datetime： 2021/5/12 13:52 
# File ：forms.py
from django import forms
from django.contrib.auth.models import User


# 登录表单，继承了form.Form类
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
