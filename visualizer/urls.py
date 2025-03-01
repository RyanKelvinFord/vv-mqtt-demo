from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('get-mock-data/', views.get_mock_data, name='get_mock_data'),
    path('download-csv/', views.download_csv, name='download_csv'),
]