from django.shortcuts import render, get_object_or_404
from django.db import models
from django.contrib.auth import authenticate, logout
from polls.models import PollUser
from polls.models import ApiKey
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from polls.models import Doctor, Choice


def auth(obj):
        username = obj.session.get('username')
        api_key = obj.session.get('api_key')
        is_auth = True
        context = {}
        try:
            puser = PollUser.objects.get(user__username=username)
            apk = ApiKey.objects.get(user=puser, api_key=api_key)
        except PollUser.DoesNotExist:
            is_auth = False
            context = {'error': 'User not found with given username'}
        except ApiKey.DoesNotExist:
            is_auth = False
            context = {'error': 'ApiKey does not match'}
        else:
            context = {
                'name': "{} {}".format(puser.user.first_name, puser.user.last_name),
                'username': username,
                'user_id': puser.id
            }

        return is_auth, context



def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        print(request.POST)

        user = User.objects.create_user(username=request.POST['username'], 
                                password=request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        puser = PollUser(user=user)
        puser.save()

        import string
        import random 

        ApiKey(user=puser, api_key=''.join(random.choice(string.ascii_lowercase) for i in range(16))).save()

        return HttpResponseRedirect("/api/login")

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            puser = PollUser.objects.get(user=user, is_removed=False)
            api_key = ApiKey.objects.get(user=puser)
            # redirect to home page with HttpResponseRedirect
            request.session['username'] = user.username
            request.session['api_key'] = api_key.api_key
            return HttpResponseRedirect("/home")
        else:
            return render(request, 'login.html', context={'error_message': 'Wrong username or password'})

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/api/login")


def doctors(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctors.html', context)

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

def vote_choice(request, choice_id):
    if request.method == 'POST':
        # Get the choice object
        choice = Choice.objects.get(pk=choice_id)
        # Increment the votes
        choice.votes += 1
        # Save the updated choice
        choice.save()
        # Set a success message
        message = "Voted Successfully!"
        # Redirect to a success page or render a template with a success message
        return render(request, 'selecte.html')