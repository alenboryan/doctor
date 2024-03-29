from django.contrib import admin
from django.urls import path
from api.views import register, login, log_out
from api.views import doctors , doctor_detail, vote_choice
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register', register),
    path('api/login', login),
    path('api/logout', log_out),
    path('api/doctors', doctors, name='doctors'), 
    path('api/doctors/<int:doctor_id>/', doctor_detail, name='doctor_detail'),
    path('api/vote/<int:doctor_id>/', vote_choice, name='vote_choice')
]
