from django.shortcuts import render
from customer.models import Users,Bookings,Feedbacks,Messages

# Create your views here.

def admin_login(request):
    return render(request,'admi/login.html')

def dashboard(request):
    totalObj = Bookings.objects.count()
    feedbacksObj = Feedbacks.objects.count()
    pendingObj = Bookings.objects.filter(status="Pending").count()
    completedObj = Bookings.objects.filter(status="Competed").count()
    return render(request,'admi/dashboard.html',{'total':totalObj,'pending':pendingObj,'completed':completedObj,'feedbacks':feedbacksObj})

def total_booking(request):
    bookingsObj = Bookings.objects.all()
    return render(request,'admi/total-booking.html',({'data':bookingsObj}))

def completed_booking(request):
    bookingsObj = Bookings.objects.filter(status="Completed")
    return render(request,'admi/completed_booking.html',({'data':bookingsObj}))

def pending_booking(request):
    bookingsObj = Bookings.objects.filter(status="Pending")
    return render(request,'admi/pending_bookings.html',({'data':bookingsObj}))

def employee_register(request):
    return render(request,'admi/employee_registration.html')

def employee_management(request):
    return render(request,'admi/employee_management.html')

def service_history(request):
    bookingsObj = Bookings.objects.filter(status="Completed")
    return render(request,'admi/service_history.html',({'data':bookingsObj}))

def feedbacks(request):
    feedbackObj = Feedbacks.objects.all()
    return render(request,'admi/feedbacks.html',({'data':feedbackObj}))

def messages(request):
    messagesObj = Messages.objects.all()
    return render(request,'admi/messages.html',({'data':messagesObj}))