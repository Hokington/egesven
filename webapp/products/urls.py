from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='list'),
    path('crear/', views.product_create, name='create'),
    path('editar/<int:pk>/', views.product_edit, name='edit'),
    path('eliminar/<int:pk>/', views.product_delete, name='delete'),
]
