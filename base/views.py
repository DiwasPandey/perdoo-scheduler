from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django_celery_results.models import TaskResult
from datetime import datetime
from dateutil import parser
from .models import Event   
from .forms import EventForm
from .tasks import send_request


def home(request):
    page = 'home'
    context = {'page': page}
    return render(request, 'main.html', context)


def register(request):
    page = 'register'
    form = UserCreationForm()
    context = {'form': form, 'page': page}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    return render(request, 'base/login_register.html', context)


def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
    return render(request, 'base/login.html')

def logoutUser(request):
    logout(request)
    redirect('home')

@login_required(login_url='login')
def createEvent(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        try:
            date = parser.parse(form['datetime'])  
            print(date)
            if form.is_valid():
                event = form.save()
                send_request.delay(event.toJSON())
                return redirect('home')  
        except:
            messages.error(request, 'Please enter a valid date')
            context = {'form': form}
            return render(request, 'base/login.html', context)

    context = {'form': form}
    return render(request, 'base/create_event.html', context)


def async_func(request):
   return send_request.delay("2022 09 05 01:37:45")
    

def pending_request(request):
    events = Event.objects.all()
    pending = []
    for event in events:
        if (parser.parse(event.datetime) - datetime.now()).total_seconds() > 0:
            pending.append(event)

    context = {'pending': pending}
    return render(request, 'base/pending.html', context)


def update_event(request, id):
    event = Event.objects.get(id=id)
    form = EventForm(instance=event)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('pending')

    context = {'form': form}
    return render(request, 'base/create_event.html', context)

def results(request):
    results = TaskResult.objects.all()

    return render(request, 'base/results.html', context={'results':results})
