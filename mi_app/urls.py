from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola_mundo, name='hola_mundo'),
    path('dashboard/', views.dashboard_power_bi, name='dashboard_power_bi'), # Nueva ruta para el dashboard de Power BI
]
