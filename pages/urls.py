from django.urls import path
from .import views

urlpatterns = [
    path('', views.masterpage,name='masterpage'),
    path('SignUpAdmin.html',views.SignUpAdmin,name='SignUpAdmin'),
    path('SignUpStudent.html',views.SignUpStudents,name='SignUpStudent'),
    path('SignUpUser.html',views.SignUpUser,name='SignUpUser'),
    path('ToSignUp.html',views.ToSignUp,name='ToSignUp'),
    path('choose.html',views.choose,name='choose'),
    path('apartments.html',views.apartments,name='apartments'),
    path('oneapartment.htmml',views.oneapartment,name='oneapartment'),
    path('privateclass.html',views.privateclass,name='privateclass'),
    path('privateclass.html',views.privateclass,name='privateclass'),

]
