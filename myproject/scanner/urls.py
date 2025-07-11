# in scanner/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device-list'),       # list all devices
    path('add/', views.device_create, name='device-create'),  # create device
    path('edit/<int:pk>/', views.device_edit, name='device-edit'),  # edit device
    path('delete/<int:pk>/', views.device_delete, name='device-delete'),  # delete device
    path('export/csv/', views.export_devices_csv, name='export-devices-csv'),
    path('devices/', views.device_list, name='device-list'),

]

