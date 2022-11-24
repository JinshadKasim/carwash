from django.shortcuts import render

# Create your views here.

def admin_login(request):
    return render(request,'admi/login.html')

def dashboard(request):
    return render(request,'admi/dashboard.html')

def total_booking(request):
    return render(request,'admi/total-booking.html')

def completed_booking(request):
    return render(request,'admi/completed_booking.html')

def employee_management(request):
    return render(request,'admi/employee_management.html')

def service_history(request):
    return render(request,'admi/service_history.html')