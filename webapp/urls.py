from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.buscar_producto, name='buscar_producto'),
    path('producto/<int:id>', views.detalle_producto, name='detalle_producto'),
    path('carrito/', views.carrito, name="carrito"),
    path('checkout/', views.checkout, name="checkout"),
    path('register/',views.register, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/',  views.logoutView, name='logout'),
    path('admin/',views.adminView, name='admin'),

    # Products CRUD
    path('admin/productos/', include('webapp.products.urls')),
]