from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'customer/index.html')

def login(request):
    return render(request,'customer/login.html')

def contact(request):
    return render(request,'customer/contact.html')
    
def signedin(request):
    return render(request,'customer/signedin.html')
    
    
def booking(request):
    return render(request,'customer/booking.html')
    
    
def status(request):
    return render(request,'customer/status.html')
    