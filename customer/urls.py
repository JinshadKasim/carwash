from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register',views.register,name='reg'),
    path('contact',views.contact,name='contact'),
    path('home',views.signedin,name='home'),
    path('booking',views.booking,name='booking'),
    path('status',views.status,name='status'),
    path('email_check',views.checkEmail,name='email_check'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('insert_data',views.insertData,name='insert_data'),
    path('insert_message',views.insertMessage,name='insert_message'),
    path('insert_feedback',views.insertFeedback,name='insert_feedback'),
    path('edit_data',views.editData,name='edit_data'),
    path('delete_booking',views.deleteData,name='delete_booking'),
    path('cancel_booking/<int:id>',views.cancel_booking,name='cancel_booking'),


]
