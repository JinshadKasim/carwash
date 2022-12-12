from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
     path('employee_login',views.emp_employee_login,name='employee'),
     path('dashboard',views.emp_dashboard,name='dashboard'),
     path('total_booking',views.emp_total_booking,name='tbooking'),
     path('completed_booking',views.emp_completed_booking,name='cbooking'),
     path('pending_booking',views.emp_pending_booking,name='pbooking'),
     path('employee_register',views.emp_employee_register,name='employee_register'),
     path('employee_management',views.emp_employee_management,name='employee_management'),
     path('Service History',views.emp_service_history,name='serviceHistory'),
     path('feedbacks',views.emp_feedbacks,name='feedbacks'),
     path('messages',views.emp_messages,name='messages'),
]