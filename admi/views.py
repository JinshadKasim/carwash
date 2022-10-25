from django.shortcuts import render

# Create your views here.

def admin_login(request):
    return render(request,'admi/login.html')

def dashboard(request):
    return render(request,'admi/dashboard.html')

def total_booking(request):
    return render(request,'admi/total-booking.html')