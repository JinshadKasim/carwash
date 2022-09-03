from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('Login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('home',views.signedin,name='home'),
    path('booking',views.booking,name='booking'),
]
