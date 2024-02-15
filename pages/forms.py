from django import forms
from .models import SignUp


class SignUpForm(forms.Form):

   # class Meta:
    #    model=SignUp
     #   fields=['Username','Email','Password','Re_Password']
      #  labels={

       #     'Username':'Username',
        #    'Email':'Email',
         #   'Password':'Password',
          #  'Re_Password':'Re_Password'

        #}
        #widgets={
         #   'Username' : forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
          #  'Email': forms.EmailInput(attrs={'class':'form-control'}),
           # 'Passsword':forms.TextInput(attrs={'class':'form-control','type':'password'}),
            #'Re_Password':forms.TextInput(attrs={'class':'form-control','type':"password"}),
       # }
     Username=forms.CharField(max_length=100)
     Email=forms.CharField(max_length=100)
     Password=forms.CharField(max_length=100)
     Re_Password=forms.CharField(max_length=100)
        

    #def __str__(self):
       # return self.Username
        