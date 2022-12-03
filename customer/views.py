from django.shortcuts import render,redirect
from customer.models import Users,Bookings
from decorators import login_check,logout_check
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict




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
    user = Users.objects.get(id=request.session['userId'])
    user_bookings = Bookings.objects.filter(user_id=request.session['userId'])
    print(user_bookings)

    return render(request,'customer/status.html',{'bookings':user_bookings,'user':user})
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


@csrf_exempt
def insertData(request):
        plan = request.POST.get('plan')
        phone = request.POST.get('phone')
        car_name = request.POST.get('car_name')
        destination = request.POST.get('destination')
        washing_date = request.POST.get('washing_date')
        hour = request.POST.get('hour')
        minute = request.POST.get('minute')
        ampm = request.POST.get('ampm')
        message = request.POST.get('message')
        current_user = request.session.get('userId')
        print(plan)
        print(phone)
        print(car_name)
        print(destination)
        print(washing_date)
        print(hour)
        print(minute)
        print(ampm)
        print(message)
        bookingObj = Bookings(plan=plan, phone=phone, car_name=car_name, destination=destination, washing_date=washing_date,hour=hour,minute=minute, ampm=ampm, message=message, user_id=current_user)
        bookingObj.save()
        print('Booking Success')
        return JsonResponse({'message':'Service Booked Successfully'})


def cancelBooking(request,id=0):
    bookingObj = Bookings.objects.get(id = id).delete()
    return redirect('status')
    

def editData(request,id=0):
    id = request.POST.get('id')
    data = Bookings.objects.get(id=id)
    model_to_dict(data)
    print(data)

    return JsonResponse({'data': data})