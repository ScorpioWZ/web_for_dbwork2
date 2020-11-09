# -*- coding: utf-8 -*-

'''
@Time    : 2020/11/9 23:32
@Author  : Wanhao Zhang
@Contact : 1809721229@qq.com 
@FileName: urls.py
@Software: PyCharm
 
'''
from django.urls import path

from web_for_dbwork2 import views

urlpatterns = [
    path('', views.index, name='index'),
]