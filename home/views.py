from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import UserActivity
from django.contrib.auth.decorators import login_required
# Create your views here.

def dashboard(request):
        if request.user.is_authenticated:
                context = UserActivity.objects.filter(user = request.user)
                return render(request, 'home/welcome.html',{'act':context})
        else:   
                messages.warning(request,'You first have to login')
                return redirect('/')

def session(request):
        return render(request,'home/dashboard.html')


@login_required(login_url='accounts/login')
def add_activity(request):
        if request.method == 'POST':
                pass
                
        else:
                return render(request, 'home/activity.html')
