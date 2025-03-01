from django.urls import path
from . import views

urlpatterns = [
    # Simulator endpoints
    path('dashboard/', views.dashboard, name='dashboard'),
    path('get-mock-data/', views.get_mock_data, name='get_mock_data'),
    path('download-csv/', views.download_csv, name='download_csv'),

    # Motor endpoints
    path('motor-dashboard/', views.motor_dashboard, name='motor_dashboard'),
    path('get-motor-data/', views.get_motor_data, name='get_motor_data'),
    path('download-motor-csv/', views.download_motor_csv, name='download_motor_csv'),

    # MQTT endpoints
    path('mqtt-data/', views.mqtt_data_endpoint, name='mqtt_data_endpoint'),
    path('get-mqtt-data/', views.get_mqtt_data, name='get_mqtt_data'),
    path('mqtt-dashboard/', views.mqtt_dashboard, name='mqtt_dashboard'),
]