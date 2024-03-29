from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User


class PollUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    is_removed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@admin.register(PollUser)
class PollUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_info', 'registered_at']

    def get_user_info(self, obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name)
    get_user_info.short_description = 'User'

class ApiKey(models.Model):
    user = models.OneToOneField(PollUser, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=16)

    def __str__(self):
        return "{} {}".format(self.user.user.username, self.api_key)

@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_info', 'api_key']

    def get_user_info(self, obj):
        return obj.user.user.username
    get_user_info.short_description = 'User'
    
      
class Doctor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def to_dict(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'profession': self.profession,  
            'pub_date': self.pub_date
        }

class PatientTime(models.Model):
    user = models.ManyToManyField(Doctor)

    def __str__(self):
        return f"Patient appointment with {self.doctor}"
class Choice(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    text = models.CharField(max_length=50, default="Default Text")  # Provide a default value here
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.doctor} - {self.text} - {self.votes}"

    def to_dict(self):
        return {
            'id': self.id,
            'doctors': str(self.doctor),
            'votes': self.votes,
            'text': self.text,
        }

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'text', 'votes']

    def question_info(self, obj):
        return obj.question.question_text
    question_info.short_description = 'Doctor'
    
    
