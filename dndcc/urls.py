from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ccindex, name='ccindex'),
    path('register/', views.ccregister, name='ccregister'),
    path('login/', views.cclogin, name='cclogin'),
    path('logout/', views.cclogout, name='cclogout'),
    path('new_character/', views.new_character, name='new_character'),
    path('delete_character/', views.delete_character, name='delete_character'),
    path('char/', views.character, name='character'),
    path('update', views.ccupdate, name='ccupdate'),
    path('weapon/', views.weapon, name='weapon'),
    path('spell/', views.spell, name='spell'),
    path('delete_spell/', views.delete_spell, name='delete_spell'),
    path('delete_weapon/', views.delete_weapon, name='delete_weapon'),
    path('combat/', views.combat, name='combat'),
    path('init/', views.init, name='init'),
    path('weapon_attack/', views.weapon_attack, name='weapon_attack'),
    path('spell_attack/', views.spell_attack, name='spell_attack'),
    path('saving_throw/', views.saving_throw, name='saving_throw'),
]