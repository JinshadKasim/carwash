from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from customer.models import Users,Bookings,Feedbacks,Messages

# Create your views here.

def emp_employee_login(request):
    return render(request,'employee/login.html')

def emp_dashboard(request):
    feedbacksObj = Feedbacks.objects.count()
    totalObj = str(Bookings.objects.count())
    pendingObj = str(Bookings.objects.filter(status="Pending").count())
    completedObj = str(Bookings.objects.filter(status="Competed").count())
    return render(request,'employee/dashboard.html',{'total':totalObj,'pending':pendingObj,'completed':completedObj,'feedbacks':feedbacksObj})

def emp_total_booking(request):
    bookingsObj = Bookings.objects.all()
    return render(request,'employee/total-booking.html',({'data':bookingsObj}))

def emp_completed_booking(request):
    bookingsObj = Bookings.objects.filter(status="Completed")
    return render(request,'employee/completed_booking.html',({'data':bookingsObj}))

def emp_pending_booking(request):
    bookingsObj = Bookings.objects.filter(status="Pending")
    return render(request,'employee/pending_bookings.html',({'data':bookingsObj}))

def emp_employee_register(request):
    return render(request,'employee/employee_registration.html')

def emp_employee_management(request):
    return render(request,'admemployeei/employee_management.html')

def emp_service_history(request):
    bookingsObj = Bookings.objects.filter(status="Completed")
    return render(request,'employee/service_history.html',({'data':bookingsObj}))

def emp_feedbacks(request):
    feedbackObj = Feedbacks.objects.all()
    return render(request,'employee/feedbacks.html',({'data':feedbackObj}))

def emp_messages(request):
    messagesObj = Messages.objects.all()
    return render(request,'employee/messages.html',({'data':messagesObj}))