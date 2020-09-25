"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

#from website
from django.conf import settings
from django.conf.urls.static import static


#patterns to match e.g. 'about/' and sending it to blog.urls for 
#further processing, it will chop out matched part and mathes the rest
#in this case 'about'; while in blog.urls it finds route 'about' and the 
#function that manages it is: views.about which has HttpResponse 

#here we can update paths e.g. to admin_dev/ and it will be automatically
#updated in our browser where we runserver

#blog page is now the home page of our website, thats why is empty path
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)