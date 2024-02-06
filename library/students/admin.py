from django.contrib import admin
from students.models import CustomUser
# Register your models here.
from django.http import HttpRespose
admin.site.register(CustomUser)
