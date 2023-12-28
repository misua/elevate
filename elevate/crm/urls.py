from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register/', views.register, name='register'),
    
    path('task/', views.task, name='task'),

    path('task-form/', views.task_form, name='task-form'),
   
]
