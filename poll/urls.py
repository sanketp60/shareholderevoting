from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('vote/<str:pollid>', views.vote, name='vote'),
    path('profile/', views.profile, name='profile'),
    path('vote/register/', views.vote_register, name='vote-register'),
]