# tasks/urls.py
from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.TaskViewSet, basename='task')


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/update/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'), 
    path('<int:pk>/complete/', views.task_complete, name='task_complete'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
]
