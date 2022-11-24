from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
     path('admi',views.admin_login,name='admi'),
     path('dashboard',views.dashboard,name='dashboard'),
     path('total_booking',views.total_booking,name='tbooking'),
     path('completed_booking',views.completed_booking,name='cbooking'),
     path('Employee Management',views.employee_management,name='employeeManagement'),
     path('Service History',views.service_history,name='serviceHistory'),
]