# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:09:58 2020

@author: Rob
"""

from django.urls import path
from . import views

#matched patterns withing given functions in views.py 
urlpatterns = [
    path('', views.home, name='blog-home'), 
    path('about/', views.about, name='blog-about'), 

]