from django.shortcuts import render,redirect
from customer.models import Users
from decorators import login_check,logout_check
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




# Create your views here.

@logout_check
def index(request):
    return render(request,'customer/index.html')

@logout_check
def register(request):
    print("iam world")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        userObj = Users(name=name, email=email, phone=phone, password=password)
        userObj.save()
    
    return render(request,'customer/login.html')

@csrf_exempt   
def checkEmail(request):
    email = request.POST.get('email')
    print(email)
    emailExist = Users.objects.filter(email = email).exists()
    print(emailExist)
    return JsonResponse({"message":emailExist})


def contact(request):
    return render(request,'customer/contact.html')

@login_check    
def signedin(request):
    return render(request,'customer/signedin.html')
    
@login_check
def booking(request):
    return render(request,'customer/booking.html')
    
@login_check
def status(request):
    return render(request,'customer/status.html')
@logout_check    
def login(request):
    print("Hello world")
    user = Users.objects.all()
    print(user)

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']  
        try:
            user = Users.objects.get(email=email,password=password)
            # if user.email == username and user.password == password:
            request.session['userId'] = user.id
            print(request.session['userId'])
            return render(request,'customer/signedin.html')

        except Exception as e:
            print(e)
            return render(request,'customer/login.html',{'message':'Invalid Email or Password'})

    
    # print(username)
    # print(password)
    return render(request,'customer/login.html')


def logout(request):
    del request.session['userId']
    return render(request, 'customer/index.html')
