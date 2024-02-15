from django.shortcuts import render ,redirect
from django . contrib.auth.forms import UserCreationForm


#from .forms import ProfileForm
from django.contrib import messages
#from .models import UploadFile
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import SignUp
from .models import Apartments
from .forms import SignUpForm

def masterpage(request):
    return render(request,'masterpage.html')


def SignUpAdmin(request):
     username=request.POST.get('Username')
     email=request.POST.get('Email')
     password=request.POST.get('Password')
     re_Password=request.POST.get('Re_Password')
     data=SignUp(Username=username,Email=email,Password=password,Re_Password=re_Password)
     data.save()
     return render(request,'pages/SignUpAdmin.html',{'SignUpForm':SignUpForm})
           
       


def SignUpStudents(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Re_Password = request.POST.get('Re_Password')
        # Call the SignUp function with the correct arguments
        new_SignUp = SignUp(Username=Username, Email=Email, Password=Password, Re_Password=Re_Password)
        #data= SignUp(Username=Username, Email=Email, Password1=Password1, RE_Password=RE_Password)
        #data.save();
        new_SignUp.save()

        return render(request,'pages\SignUpStudent.html')
    else:
            # Handle GET request
        return render(request, 'pages\SignUpUser.html')




def SignUpUser(request):
    #if request.method == 'POST':
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Re_Password = request.POST.get('Re_Password')
        # Call the SignUp function with the correct arguments
        new_SignUp = SignUp.objects.create(Username=Username, Email=Email, Password=Password, Re_Password=Re_Password)
        #data= SignUp(Username=Username, Email=Email, Password1=Password1, RE_Password=RE_Password)
        #data.save();
        new_SignUp.save()

        return render(request,'pages\SignUpUser.html',{'SignUp':new_SignUp})
    #else:
            # Handle GET request
        #return render(request, 'pages\SignUpUser.html')
    




def ToSignUp(request):
    return render(request,'pages\ToSignUp.html')


def choose(request):
     return render(request,'pages\choose.html')


def apartments (request):
     apart=Apartments.objects.all()
     return render(request,'pages/apartments.html',{'apartments':apartments})


def oneapartment(request):
     return render(request,'pages\oneapartment.html')

def privateclass(request):
     return render(request,'pages/privateclass.html')