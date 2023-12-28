from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('views-tasks/', views.tasks, name='views-tasks'),
    
    path('register/', views.register, name='register'),
    
    path('create-task/', views.create_task, name='create-task'),
   
]
