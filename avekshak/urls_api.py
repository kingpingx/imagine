from django.urls import path
from mainapp import views_api

urlpatterns = [
    path('users/', views_api.UserViewset.as_view()),
    path('user/<username>/', views_api.User_data.as_view())
]
