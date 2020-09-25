# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:09:58 2020

@author: Rob
"""

from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView)

#matched patterns withing given functions in views.py 
urlpatterns = [
    #path('', views.home, name='blog-home'),  #regular
    path('', PostListView.as_view(), name='blog-home'),
    #route
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    #update
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    #delete
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'), 

]

