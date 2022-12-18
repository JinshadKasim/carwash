from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from customer.models import Users, Bookings, Feedbacks, Messages
from employee.models import Employees
from django.http import JsonResponse
from decorators import emp_login_check, emp_logout_check


# Create your views here.

@emp_logout_check
def emp_employee_login(request):

    if request.method == 'POST':
        username = request.POST['emp_username']
        password = request.POST['emp_password']
        try:
            # employeeObj = Employees.objects.get(emp_email=username)
            # print(employeeObj)
            employeeObj = Employees.objects.get(
                emp_phone=username, emp_password=password)
            # if employeeObj.emp_phone == username and employeeObj.emp_password==password:
            request.session['empId'] = employeeObj.id
            request.session['empPhoto'] = employeeObj.emp_photo.url
            print(request.session['empId'])
            print("Hello world")
            return redirect('emp_dashboard')

        except Exception as e:
            print(e)
            return render(request, 'employee/login.html', {'message': 'Invalid Email or Password'})

    return render(request, 'employee/login.html')


def emp_employee_logout(request):
    del request.session['empId']
    return redirect('employee_login')


@emp_login_check
def emp_dashboard(request):
    feedbacksObj = Feedbacks.objects.count()
    totalObj = str(Bookings.objects.count())
    empObj = Employees.objects.get(id=request.session['empId'])
    pendingObj = str(Bookings.objects.filter(status="Pending").count())
    completedObj = str(Bookings.objects.filter(status="Completed").count())
    context =  {
        'total': totalObj, 
        'pending': pendingObj, 
        'completed': completedObj, 
        'feedbacks': feedbacksObj, 
        'data':empObj
        }
    return render(request, 'employee/dashboard.html',context)


def emp_total_booking(request):
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

    
        return redirect('emp_tbooking')
    
    return render(request, 'employee/total-booking.html', ({'data': bookingsObj}))


def emp_completed_booking(request):
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

    
        return redirect('emp_cbooking')

    return render(request, 'employee/completed_booking.html', ({'data': bookingsObj}))


def emp_pending_booking(request):
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

    
        return redirect('emp_pbooking')

    return render(request, 'employee/pending_bookings.html', ({'data': bookingsObj}))


def emp_employee_register(request):
    return render(request, 'employee/employee_registration.html')


def emp_employee_management(request):
    return render(request, 'admemployeei/employee_management.html')


def emp_service_history(request):
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

    
        return redirect('emp_serviceHistory')

    return render(request, 'employee/service_history.html', ({'data': bookingsObj}))


def emp_feedbacks(request):
    feedbackObj = Feedbacks.objects.all()
    return render(request, 'employee/feedbacks.html', ({'data': feedbackObj}))


def emp_messages(request):
    messagesObj = Messages.objects.all()
    return render(request, 'employee/messages.html', ({'data': messagesObj}))


def emp_change_password(request):
    if request.method == 'POST':
        print("Hello")
        oldpassword = request.POST['oldpassword']
        newpassword = request.POST['newpassword']
        empObj = Employees.objects.get(id=request.session['empId'])
        try:
            if empObj.emp_password == oldpassword:
                Employees.objects.filter(id=request.session['empId']).update(
                    emp_password=newpassword)
                return render(request, 'employee/change_password.html')

        except Exception as e:
            print(e)
            return render(request, 'employee/change_password.html', {'message': 'Old Password is Incorrect'})

    return render(request, 'employee/change_password.html')

def emp_profile(request):
    print(request.session['empId'])
    empObj = Employees.objects.get(id=request.session['empId'])
    return render(request, 'employee/profile.html', {'data': empObj})


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
    return redirect("emp_dashboard")



def emp_delete_message(request,id=0):
    Messages.objects.get(id=id).delete()
    return redirect('emp_messages')


def emp_delete_feedback(request,id=0):
    Feedbacks.objects.get(id=id).delete()
    return redirect('emp_feedbacks')


@emp_login_check
def emp_customers(request):
    customersObj = Users.objects.all()
    return render(request,'employee/emp_customers.html',({'data':customersObj}))
