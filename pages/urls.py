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
    path('more.html',views.more,name='more'),
    path('aboutus.html',views.aboutus,name='aboutus'),
    path('addapartment.html',views.addapartment,name='addapartment'),
    path('scolarshipswith.html',views.scolarshipswith,name='scolarships'),

    # path('adminapartments.html',views.adminapartments,name='adminapartments'),
    # path('forstudentsusers.html',views.forstudentsusers,name='forstudentsusers'),
    # path('departmentcourses.html',views.departmentcourses,name='departmentcourses'),
    # path('showSoftwarclasses.html',views.showSoftwarclasses,name="showSoftwarclasses"),
    # path('showchemicalclasses.html',views.showchemicalclasses,name="showchemicalclasses"),
    # path('showmechanicalclasses.html',views.showmechanicalclasses,name="showmechanicalclasses"),
    # path('showelectricclasses.html',views.showelectricclasses,name="showelectricclasses"),
    # path('showcivilclasses.html',views.showcivilclasses,name="showcivilclasses"),