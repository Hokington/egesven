from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='list'),
    path('crear/', views.user_create, name='create'),
    path('editar/<int:pk>/', views.user_edit, name='edit'),
    path('eliminar/<int:pk>/', views.user_delete, name='delete'),
]
