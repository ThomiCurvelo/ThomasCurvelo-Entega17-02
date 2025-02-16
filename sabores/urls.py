from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_sabor, name='agregar_sabor'),
    path('listar/', views.listar_sabores, name='listar_sabores'),
    path('buscar/', views.buscar_sabores, name='buscar_sabores'),
]
