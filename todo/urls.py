from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_home, name='todo_home'),
    path('add/', views.todo_add, name='todo_add'),
    path('<int:pk>/add_step/', views.todo_add_step, name='todo_add_step'),
    path('<int:pk>/complete/', views.todo_complete, name='todo_complete'),
    path('<int:pk>/uncheck/', views.todo_uncheck, name='todo_uncheck'),
    path('<int:pk>/delete/', views.todo_delete, name='todo_delete'),
    path('<int:pk>/complete_step/', views.todo_complete_step, name='todo_complete_step'),
    path('<int:pk>/delete_step/', views.todo_delete_step, name='todo_delete_step'),
]