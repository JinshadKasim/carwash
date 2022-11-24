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