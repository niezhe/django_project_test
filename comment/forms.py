#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： jenny
# datetime： 2021/10/28 15:52 
# File ：forms.py
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
