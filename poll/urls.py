from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/<str:pollid>', views.vote, name='vote'),
    path('profile/', views.profile, name='profile'),
]