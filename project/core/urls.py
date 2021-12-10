from django.contrib import admin
from core import views
from django.urls import path, include
urlpatterns = [
    path('bmi/', views.bmi),
    path('measurement/', views.bmi_measurement),
    path('measurements/', views.measurements, name="all_measurements"),
    path('measurements/<int:id>/', views.measurement, name="delete_measurement"),
]