from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Blackjack/', views.BJ, name='BJ'),
]