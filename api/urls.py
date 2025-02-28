from django.urls import path
from . import views

urlpatterns = [
    
    path('materials/', views.MaterialList.as_view(), name='materials'),

]