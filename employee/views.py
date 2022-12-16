from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from customer.models import Users, Bookings, Feedbacks, Messages
from employee.models import Employees
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
    pendingObj = str(Bookings.objects.filter(status="Pending").count())
    completedObj = str(Bookings.objects.filter(status="Competed").count())
    return render(request, 'employee/dashboard.html', {'total': totalObj, 'pending': pendingObj, 'completed': completedObj, 'feedbacks': feedbacksObj})


def emp_total_booking(request):
    bookingsObj = Bookings.objects.all()
    return render(request, 'employee/total-booking.html', ({'data': bookingsObj}))


def emp_completed_booking(request):
    bookingsObj = Bookings.objects.filter(status="Completed")
    return render(request, 'employee/completed_booking.html', ({'data': bookingsObj}))


def emp_pending_booking(request):
    bookingsObj = Bookings.objects.filter(status="Pending")
    return render(request, 'employee/pending_bookings.html', ({'data': bookingsObj}))


def emp_employee_register(request):
    return render(request, 'employee/employee_registration.html')


def emp_employee_management(request):
    return render(request, 'admemployeei/employee_management.html')


def emp_service_history(request):
    bookingsObj = Bookings.objects.filter(status="Completed")
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
    return render(request, 'employee/profile.html', ({'data': empObj}))
