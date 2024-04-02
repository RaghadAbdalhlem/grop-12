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
from .forms import addApartmentform
from django.shortcuts import redirect
from .forms import addclassesform,addelectricclassesform,addcivilclassesform,addchemicalclassesform,addscholarshipform,addmechanicalclassesform,addApartmentform,addscholarshipform,updateApartmentform,updatescholarshipform,updatesoftwarform,updatecivilform,updateelectricform,updatechemicalform,updatemechanicalform
from .models import PrivateMechanicalClasses,PrivateCivilClasses,PrivateChemicalClasses,PrivateElectricClasses,PrivateClasses,scholarship
from .filters import PrivateClassesFilter
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group
from django.contrib.auth import logout,login
from django.contrib.auth.forms import UserCreationForm
from .models import SignUp
from .forms import CreatUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages

def masterpage(request):
    return render(request,'masterpage.html')
def more(request):
    return render(request,'more.html')
    

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

def SignUpAdmin(request):
     form=SignUpForm
     username=request.POST.get('Username')
     email=request.POST.get('Email')
     password=request.POST.get('Password')
     re_Password=request.POST.get('Re_Password')
     data=SignUp(Username=username,Email=email,Password=password,Re_Password=re_Password)
     data.save()
     conaxt=fo
     return render(request,'pages/SignUpAdmin.html',{'SignUpForm':SignUpForm})

def Logiadmin(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            users_in_group = Group.objects.get(name='Admin').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('foradmin')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'pages/Loginadmin.html', context)
       
def update_student():
     pass

def SignUpStudents(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Re_Password = request.POST.get('Re_Password')
        # Call the SignUp function with the correct arguments
        new_SignUp = SignUp(Username=Username, Email=Email, Password=Password, Re_Password=Re_Password)
        #data= SignUp(Username=Username, Email=Email, Password1=Password1, RE_Password=RE_Password)
        # data.save();
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
def aboutus(request):
    return render(request,'pages/aboutus.html')


def addapartment(request):
     form=addApartmentform()
     if request.method=='POST':
          form=addApartmentform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('addclasses')
   
     conaxt={'form':form}
     return render(request,'pages/addapartment.html',conaxt)
 
def scolarshipswith(request):
     soft=scholarship.objects.all()
     return render(request,'pages/scolarshipswith.html',{'soft':soft})

def SignUpUser(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            try:
              group =  Group.objects.get(name='Users')
            except ObjectDoesNotExist:
                group=None
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('Loginuser')
    context = {'form': form}
    return render(request, 'pages/SignUpUser.html', context)


def Loginuser(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            users_in_group = Group.objects.get(name='Users').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('forusers')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'pages/Loginuser.html', context)

# def SignUpAdmin(request):
#      form=SignUpForm()
#      # username=request.POST.get('Username')
#      # email=request.POST.get('Email')
#      # password=request.POST.get('Password')
#      # re_Password=request.POST.get('Re_Password')
#      if request.method=='POST':
#           form=SignUpForm(request.POST)

#           if form.is_valid():
#                form.save()
#                return redirect('SignUpStudent')
#     # data=SignUp(Username=username,Email=email,Password=password,Re_Password=re_Password)
#      #data.save()
#      conaxt={'form':form}
#      return render(request,'pages/SignUpAdmin.html',conaxt)



# def SignUpUser(request):
#      form=SignUpForm()
  
#      if request.method=='POST':
#           form=SignUpForm(request.POST)

#           if form.is_valid():
#                form.save()
#                return redirect('SignUpStudent')
   
#      conaxt={'form':form}
#      return render(request,'pages/SignUpUser.html',conaxt)

#         if request.method == 'POST':
#           coursename=request.POST['coursename']
#           teachername=request.POST['teachername']
#           techerphonenumber=request.POST['teacherphonenumber']
#           content=request.POST['content']
              	
        

#           new= addsoftwarclasses(coursename=coursename,teachername=teachername,techerphonenumber=techerphonenumber,content=content)   
#           new.save()   
# ################################################
#      submitted = False
#      if request.method == "POST":
#               form=addsoftwarclasses(request.POST)
#               if form.is_valid():
#                    form.save()
#                    return HttpResponseRedirect('pages/addsoftwarclasses?submitted=True')
#      else:
#              form =addsoftwarclasses 
#              if 'submitted' in request.GET:
#                    submitted=True
#      return render(request, 'pages/addsoftwarclasses.html',{'form':form,'submitted':submitted})
#      #####################################

 
def showscholarships(request):
     # soft=scholarship.objects.all()
     #,{'soft':soft}
     return render(request,'pages/showscholarships.html')


def scholarshipswith(request):
      soft=scholarship.objects.all()
     
      return render(request,'pages/scholarshipswith.html',{'soft':soft})

def scholarshipswithout(request):
     soft=scholarship.objects.all()
     return render(request,'pages/scholarshipswithout.html',{'soft':soft})


def apartmentarea(request):



  if request.method=="POST":
       searched=request.POST['searched']
       apart=Apartments.objects.filter(area=searched)

       #apart=Apartments.objects.all()
       return render(request,'pages/apartmentarea.html',{'searched':searched,'apart':apart})
  else:
        return render(request, 'pages/apartmentarea.html')



def apartmentsprice (request):

      if request.method=="POST":
       searched=request.POST['searched']
       apart=Apartments.objects.filter(price=searched)

       #apart=Apartments.objects.all()
       return render(request,'pages/apartmentsprice.html',{'searched':searched,'apart':apart})
      else:
        return render(request, 'pages/apartmentsprice.html')
def apartmentsroom (request):

      if request.method=="POST":
       searched=request.POST['searched']
       apart=Apartments.objects.filter(rooms=searched)

       #apart=Apartments.objects.all()
       return render(request,'pages/apartmentsroom.html',{'searched':searched,'apart':apart})
      else:
        return render(request, 'pages/apartmentsroom.html')


def updateapartment(request,pk):
     apartment=Apartments.objects.get(id=pk)
     form= updateApartmentform(request.POST or None , instance=apartment )
     if form.is_valid():
         form.save()
         return redirect('adminapartments')
     return render (request,'pages/updateapartment.html',{'form':form})


def updatescholarship(request,pk):
     scho=scholarship.objects.get(id=pk)
     form= updatescholarshipform(request.POST  , instance=scho )

     if form.is_valid():
         form.save()
         return redirect('adminscholarship')
     return render (request,'pages/updatescholarship.html',{'form':form})


def updatesoftwar(request,pk):
     scho=PrivateClasses.objects.get(id=pk)
     form= updatesoftwarform(request.POST or None  , instance=scho )

     if form.is_valid():
         form.save()
         return redirect('adminsoftwar')
     return render (request,'pages/updatesoftwar.html',{'form':form})
