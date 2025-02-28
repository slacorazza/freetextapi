from django.urls import path
from . import views

urlpatterns = [
    path('materials/', views.MaterialList.as_view(), name='materials'),
    path('kpis/', views.KPIList.as_view(), name='kpis'),
    path('orders/', views.OrderList.as_view(), name='orders'),
    path('inventory/', views.InventoryList.as_view(), name='inventory'),
]