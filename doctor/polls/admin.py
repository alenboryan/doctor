from django.contrib import admin
from .models import Doctor
from .models import PatientTime

from django.contrib.auth.models import User
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'profession']
    




@admin.register(PatientTime)
class PatientTimeAdmin(admin.ModelAdmin):
    filter_horizontal = ['user']



    