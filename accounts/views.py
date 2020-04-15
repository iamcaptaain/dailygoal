from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as lo
from accounts.models import User
from home.views import dashboard
from django.contrib import messages
from django.conf import settings
from django.utils.http import is_safe_url
from django.urls import reverse
from django.contrib.auth import logout 

# Create your views here.

def login(request):
    if request.method == "POST":
        a = request.POST["username"]
        b = request.POST["pass"]
        user = authenticate(request , username = a, password = b)
        next_ = request.GET.get('next',settings.LOGIN_REDIRECT_URL)
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        print(user)
        if user is not None:
            lo(request, user)
            return HttpResponseRedirect(request.GET.get('next',settings.LOGIN_REDIRECT_URL))
            
        elif User.obb.filter( username = a ).exists():
            messages.info(request,'Passward not matched')
            return redirect('/')
        
        else:
            messages.info(request,'Username and Passward not matched')
            return redirect('/')
        
    else:
        return render(request,'blog.html')

def register(request):
    if request.method == 'POST':
        pid = request.POST["username"]
        uMail = request.POST["email"]
        # uNumber = request.POST["p_number"]
        pswd = request.POST["pass"]
        pswd1 = request.POST["pass1"]

        if User.obb.filter(username = pid).exists():
            messages.info(request,'account is already exist')
        elif pswd == pswd1:
            user = User.obb.create_user(username = pid, email = uMail, password = pswd1 )
            if user is not None:
                user.save()
                messages.info(request,'Now you can login')
                return redirect('/')
            else:
                messages.info(request,'Please enter details')
                return redirect('register')
        else:
            return redirect('register')
    else:
        return render(request,'bregister.html')

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.obb.filter(username=username).exists()
    }
    return JsonResponse(data)

def validate_mail(request):
    mail = request.GET.get('mailer', None)
    data = {
        'is_taken': User.obb.filter(email=mail).exists()
    }
    return JsonResponse(data)

def out_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")