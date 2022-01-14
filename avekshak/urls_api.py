from django.urls import path
from mainapp.views_api import UserApi
from mainapp import views_api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('users/', views_api.UserViewset.as_view()),
    path('user/<username>/', views_api.User_data.as_view()),
    path('user_register/', views_api.UserApi.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
