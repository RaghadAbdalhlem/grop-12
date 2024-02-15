from django.contrib import admin
from .models import SignUp
from .models import Apartments
from .models import Private_Classes

# Register your models here.

admin.site.register(SignUp)
admin.site.register(Apartments)
admin.site.register(Private_Classes)
