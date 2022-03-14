from os import name
from django.urls import path
from Apprestapp1.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio, name="inicio"),
    path('error/',error, name="error"),
    path('contacto/', contacto, name='contacto'),
    
    path('listarestaurants/', RestaurantList.as_view(),name='List'),
    path('detallerestaurants/<pk>/', RestaurantDetail.as_view(),name='Detail'),
    path('crearrestaurants/', RestaurantCreate.as_view(),name='New'),
    path('actualizarestaurants/<pk>/', RestaurantUpdate.as_view(),name='Edit'),
    path('eliminarestaurants/<pk>/', RestaurantDelate.as_view(),name='Delete'),
    
    path('buscar/',buscar, name="buscar"),
    
    path('login/',login_request, name='Login'),
    path('register/',register,name='Register'),
    path('logout/', LogoutView.as_view(template_name='Apprestapp1/logout.html'), name = 'Logout'),
    path('editarPerfil/', editarPerfil, name = "EditarPerfil"),
]