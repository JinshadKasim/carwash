from django.shortcuts import redirect


def login_check(func):
    def wrap(request,*args,**kwargs):
        if not (request.session.get("userId")):
            return redirect("reg")
        else:
            return func(request,*args,**kwargs)
    return wrap

def logout_check(func):
    def wrap(request,*args,**kwargs):
        if  (request.session.get("userId")):
            return redirect("home")
        else:
            return func(request,*args,**kwargs)
    return wrap


def admin_login_check(func):
    def wrap(request,*args,**kwargs):
        if not (request.session.get("adminId")):
            return redirect("admin_login")
        else:
            return func(request,*args,**kwargs)
    return wrap


def admin_logout_check(func):
    def wrap(request,*args,**kwargs):
        if (request.session.get("adminId")):
            return redirect("dashboard")
        else:
            return func(request,*args,**kwargs)
    return wrap



def emp_login_check(func):
    def wrap(request,*args,**kwargs):
        if not (request.session.get("empId")):
            return redirect("employee_login")
        else:
            return func(request,*args,**kwargs)
    return wrap

def emp_logout_check(func):
    def wrap(request,*args,**kwargs):
        if (request.session.get("empId")):
            return redirect("emp_dashboard")
        else:
            return func(request,*args,**kwargs)
    return wrap