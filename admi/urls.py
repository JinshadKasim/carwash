from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
     path('',views.admin_login,name='admin_login'),
     path('admin_logout',views.admin_logout,name='admin_logout'),
     path('dashboard',views.dashboard,name='dashboard'),
     path('total_booking',views.total_booking,name='tbooking'),
     path('completed_booking',views.completed_booking,name='cbooking'),
     path('pending_booking',views.pending_booking,name='pbooking'),
     path('employee_register',views.employee_register,name='employee_register'),
     path('employee_management',views.employee_management,name='employee_management'),
     path('Service History',views.service_history,name='serviceHistory'),
     path('feedbacks',views.feedbacks,name='feedbacks'),
     path('messages',views.messages,name='messages'),
]