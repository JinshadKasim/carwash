from django.shortcuts import render,redirect
from customer.models import Users,Bookings,Feedbacks,Messages
from employee.models import Employees
from admi.models import Admins
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from random import random
from django.views.decorators.csrf import csrf_exempt
from decorators import admin_login_check,admin_logout_check


# Create your views here.

@admin_logout_check
def admin_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  
        try:
            adminObj = Admins.objects.get(username=username,password=password)
            # if user.email == username and user.password == password:
            request.session['adminId'] = adminObj.id
            print(request.session['adminId'])
            print("Hello world")
            return redirect('dashboard')

        except Exception as e:
            print(e)
            return render(request,'admi/login.html',{'message':'Invalid Email or Password'})

    
    # print(username)
    # print(password)
    return render(request,'admi/login.html')

def admin_logout(request):
    del request.session['adminId']
    return redirect('admin_login')


@admin_login_check
def dashboard(request):
    totalObj = Bookings.objects.count()
    feedbacksObj = Feedbacks.objects.count()
    pendingObj = Bookings.objects.filter(status="Pending").count()
    completedObj = Bookings.objects.filter(status="Completed").count()
    context = {
        'total':totalObj,
        'pending':pendingObj,
        'completed':completedObj,
        'feedbacks':feedbacksObj
    }
    return render(request,'admi/dashboard.html',context)

def total_booking(request):
    bookingsObj = Bookings.objects.all()

    if request.method == 'POST':
        e_id = request.POST['id']
        plan = request.POST['plan']
        phone = request.POST['phone']
        car_name = request.POST['car_name']
        destination = request.POST['destination']
        washing_date = request.POST['washing_date']
        hour = request.POST['hour']
        minute = request.POST['minute']
        ampm = request.POST['ampm']
        status = request.POST['status']
        Bookings.objects.filter(id=e_id).update(status=status, plan=plan, phone=phone, car_name=car_name, destination=destination, washing_date=washing_date,hour=hour,minute=minute, ampm=ampm)

    
        return redirect('tbooking')

    return render(request,'admi/total-booking.html',({'data':bookingsObj}))

def completed_booking(request):
    bookingsObj = Bookings.objects.filter(status="Completed")


    if request.method == 'POST':
        e_id = request.POST['id']
        plan = request.POST['plan']
        phone = request.POST['phone']
        car_name = request.POST['car_name']
        destination = request.POST['destination']
        washing_date = request.POST['washing_date']
        hour = request.POST['hour']
        minute = request.POST['minute']
        ampm = request.POST['ampm']
        status = request.POST['status']
        Bookings.objects.filter(id=e_id).update(status=status, plan=plan, phone=phone, car_name=car_name, destination=destination, washing_date=washing_date,hour=hour,minute=minute, ampm=ampm)

    
        return redirect('cbooking')


    return render(request,'admi/completed_booking.html',({'data':bookingsObj}))

@admin_login_check
def pending_booking(request):
    bookingsObj = Bookings.objects.filter(status="Pending")

    if request.method == 'POST':
        e_id = request.POST['id']
        plan = request.POST['plan']
        phone = request.POST['phone']
        car_name = request.POST['car_name']
        destination = request.POST['destination']
        washing_date = request.POST['washing_date']
        hour = request.POST['hour']
        minute = request.POST['minute']
        ampm = request.POST['ampm']
        status = request.POST['status']
        Bookings.objects.filter(id=e_id).update(status=status, plan=plan, phone=phone, car_name=car_name, destination=destination, washing_date=washing_date,hour=hour,minute=minute, ampm=ampm)

    
        return redirect('pbooking')

    return render(request,'admi/pending_bookings.html',({'data':bookingsObj}))
@admin_login_check
def employee_register(request):
    if request.method == 'POST':
        name = request.POST['emp_name']
        phone = request.POST['phone']
        email = request.POST['email']
        dob = request.POST['dob']
        address = request.POST['address']
        idproof = request.POST['idproof']
        idproofnum = request.POST['idproofnumber']
        photo = request.FILES['emp_photo']
        profile_image = str(random())+photo.name
        # add_image = FileSystemStorage()
        # add_image.save(profile_image,photo)
        userObj = Employees(emp_name=name, emp_phone=phone, emp_email=email, emp_dob=dob, emp_address=address, emp_idproof=idproof, emp_idproofnum=idproofnum, emp_photo=photo, emp_password="12345")
        userObj.save()
    
        return render(request,'admi/employee_registration.html',({'message':'Successfully Registered Employee'}))

    return render(request,'admi/employee_registration.html')

@admin_login_check
def employee_management(request):
    empObj = Employees.objects.all()
    return render(request,'admi/employee_management.html',({'data':empObj}))

@admin_login_check
def service_history(request):
    bookingsObj = Bookings.objects.filter(status="Completed")

    if request.method == 'POST':
        e_id = request.POST['id']
        plan = request.POST['plan']
        phone = request.POST['phone']
        car_name = request.POST['car_name']
        destination = request.POST['destination']
        washing_date = request.POST['washing_date']
        hour = request.POST['hour']
        minute = request.POST['minute']
        ampm = request.POST['ampm']
        status = request.POST['status']
        Bookings.objects.filter(id=e_id).update(status=status, plan=plan, phone=phone, car_name=car_name, destination=destination, washing_date=washing_date,hour=hour,minute=minute, ampm=ampm)

    
        return redirect('serviceHistory')
    return render(request,'admi/service_history.html',({'data':bookingsObj}))

@admin_login_check
def feedbacks(request):
    feedbackObj = Feedbacks.objects.all()
    return render(request,'admi/feedbacks.html',({'data':feedbackObj}))

@admin_login_check
def messages(request):
    messagesObj = Messages.objects.all()
    return render(request,'admi/messages.html',({'data':messagesObj}))

@admin_login_check
def customers(request):
    customersObj = Users.objects.all()
    return render(request,'admi/customers.html',({'data':customersObj}))

def edit_employee(request,id=0):
    empObj = Employees.objects.get(id=id)
    print(empObj.emp_dob)
    print(empObj.emp_dob.strftime('%d-%m-%y'))
    if request.method == 'POST':
        emp_id = request.POST['empl_id']
        name = request.POST['emp_name']
        phone = request.POST['phone']
        email = request.POST['email']
        dob = request.POST['dob']
        address = request.POST['address']
        idproof = request.POST['idproof']
        idproofnum = request.POST['idproofnumber']
        photo = request.POST['emp_photo']
        password = request.POST['emp_password']
        Employees.objects.filter(id=emp_id).update(emp_name=name, emp_phone=phone, emp_email=email, emp_dob=dob, emp_address=address, emp_idproof=idproof, emp_idproofnum=idproofnum, emp_photo=photo, emp_password=password)
    
        return redirect('employee_management')
    return render(request,'admi/edit_employee.html',({'data':empObj}))


@csrf_exempt   
def emp_email_check(request):
    email = request.POST.get('email')
    print(email)
    emailExist = Employees.objects.filter(emp_email = email).exists()
    print(emailExist)
    return JsonResponse({"message":emailExist})

@csrf_exempt   
def emp_number_check(request):
    phone = request.POST.get('phone')
    print(phone)
    numberExist = Employees.objects.filter(emp_phone = phone).exists()
    print(numberExist)
    return JsonResponse({"message":numberExist})


def edit_employee_data(request,id=0):
    id = request.POST.get('id')
    print(id)
    datas = Employees.objects.get(id=id)
    # model_to_dict(data)
    #print(data.car_name)
    data={'id': datas.id,'name':datas.emp_name,'phone':datas.emp_phone,'email':datas.emp_email,'dob':datas.emp_dob,'address':datas.emp_address,'idproof':datas.emp_idproof,'idproofnum':datas.emp_idproofnum,'photo':datas.emp_photo.name,'password':datas.emp_password}
    return JsonResponse({'data': data})

def delete_employee_data(request,id=0):
    print(id)
    print('fgjhfkgjnidfugdlfgjndiughdkfjbndifgh')
    Employees.objects.get(id=id).delete()
    if  (request.session.get("userId")):
        del request.session['userId']
        
    # model_to_dict(data)
    #print(data.car_name)
    return redirect('employee_management')

def delete_message(request,id=0):
    Messages.objects.get(id=id).delete()
    return redirect('messages')

def delete_feedback(request,id=0):
    Feedbacks.objects.get(id=id).delete()
    return redirect('feedbacks')

def editData(request,id=0):
    id = request.POST.get('id')
    print(id)
    datas = Bookings.objects.get(id=id)
    # model_to_dict(data)
    #print(data.car_name)
    data={'id': datas.id,'plan':datas.plan,'phone':datas.phone,'car_name':datas.car_name,'destination':datas.destination,'washing_date':datas.washing_date,'hour':datas.hour,'minute':datas.minute,'ampm':datas.ampm,'message':datas.message,'status':datas.status}
    return JsonResponse({'data': data})



def deleteData(request,id=0):
    id = request.POST.get('id')
    print(id)
    data=Bookings.objects.get(id=id)
    data = {'id':data.id}
    return JsonResponse({'data': data})

def cancel_booking(request,id=0):
    Bookings.objects.get(id=id).delete()
    return redirect("dashboard")


