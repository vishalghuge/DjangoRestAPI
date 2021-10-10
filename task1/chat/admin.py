from django.contrib import admin
from .models import *

# Register your models here.
myModels = [Users]
admin.site.register(myModels)
