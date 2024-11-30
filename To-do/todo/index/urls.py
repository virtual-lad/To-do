from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:task_id>/', views.task_details, name='task_details'),
    path('task_edit/<int:task_id>/', views.task_edit, name='task_edit'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]