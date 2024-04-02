from django.db import models
# Create your models here.
class SignUp(models.Model):


    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Re_Password=models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.Username
    class Meta:
        verbose_name='SignUp'
    

# Create your models here.
class Apartments(models.Model):

    price=models.IntegerField(null=False)
    rooms=models.IntegerField(null=False)
    area=models.CharField(max_length=100,null=False)
    content=models.TextField(null=False)
    img=models.ImageField(upload_to=())
    #def __str__(self):
     #   return self.area
    class Meta:
        verbose_name='Apartment'





class Private_Classes(models.Model):

   # cat=[
    #    'Software Engineering','Sofware Engineering',
     #   'Mechanical Engineering', 'Mechanical Engineering',
      #  'Civil Engineering','Civil Engineering',
     #   'Chemical Engineering','Chemical Engineering',
    #]
    #catigory=models.CharField(max_lengh=1000,choices=cat)
    coursename=models.CharField(max_length=50,null=True,blank=True)
    teachername=models.CharField(max_length=50,null=True,blank=True)
    teacherphonenumber=models.CharField(max_length=50,null=True,blank=True)
    content=models.CharField(max_length=100,null=True,blank=True)
    img=models.ImageField(default="static/image/personalclass.png")


class SignUp(models.Model):


    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Re_Password=models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
         return self.Username
   
     coursename=models.CharField(max_length=50,null=True,blank=True)
     teachername=models.CharField(max_length=50,null=True,blank=True)
     teacherphonenumber=models.CharField(max_length=50,null=True,blank=True)
     content=models.CharField(max_length=100,null=True,blank=True)
        #img=models.ImageField(default="static/image/personalclass.png")
     def __str__(self):
        return self.coursename   
    



    
class PrivateCivilClasses(models.Model):

    #departmentcours= models.CharField(max_length=100)
    coursename=models.CharField(max_length=50,null=True,blank=True)
    teachername=models.CharField(max_length=50,null=True,blank=True)
    teacherphonenumber=models.CharField(max_length=50,null=True,blank=True)
    content=models.CharField(max_length=100,null=True,blank=True)
    #img=models.ImageField(default="static/image/personalclass.png")
    # def __str__(self):
    #     return self.departmentcours
    def __str__(self):
        return self.coursename   



class PrivateElectricClasses(models.Model):

    #departmentcours= models.CharField(max_length=100)
    coursename=models.CharField(max_length=50,null=True,blank=True)
    teachername=models.CharField(max_length=50,null=True,blank=True)
    teacherphonenumber=models.CharField(max_length=50,null=True,blank=True)
    content=models.CharField(max_length=100,null=True,blank=True)
    #img=models.ImageField(default="static/image/personalclass.png")
    # def __str__(self):
    #     return self.departmentcours




class PrivateMechanicalClasses(models.Model):

    #departmentcours= models.CharField(max_length=100)
    coursename=models.CharField(max_length=50,null=True,blank=True)
    teachername=models.CharField(max_length=50,null=True,blank=True)
    teacherphonenumber=models.CharField(max_length=50,null=True,blank=True)
    content=models.CharField(max_length=100,null=True,blank=True)
    #img=models.ImageField(default="static/image/personalclass.png")
    # def __str__(self):
    #     return self.departmentcours







class PrivateChemicalClasses(models.Model):

   # departmentcours= models.CharField(max_length=100)
    coursename=models.CharField(max_length=50,null=True,blank=True)
    teachername=models.CharField(max_length=50,null=True,blank=True)
    teacherphonenumber=models.CharField(max_length=50,null=True,blank=True)
    content=models.CharField(max_length=100,null=True,blank=True)
    #img=models.ImageField(default="static/image/personalclass.png")
    # def __str__(self):
    #      return self.departmentcours

