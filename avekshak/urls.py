"""avekshak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include ,path
from mainapp.views import *
from mainapp import views

from django.contrib.auth import views as auth_views
from rest_framework import routers

# routers = routers.DefaultRouter()
# routers.register(r'details', views.UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GeneralPageView.as_view()),
    path('home', HomeView.as_view()),
    # path('user', include(routers.urls)),
    # path('api_auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('avekshak.urls_api')),
    path('base', views.base),
    path('login', LoginView.as_view(), name="login"),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('change_password/<token>/', views.change_password, name='change_password'),
    path('register', RegisterView.as_view()),
    path('logout', LogoutView.as_view()),
]
