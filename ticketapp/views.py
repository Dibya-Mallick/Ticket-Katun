from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Bus,Details,ContactInfo,ReserveInfo
from .forms import DetailsForm,ContactInfoForm,ReserveInfoForm

# Create your views here.
def index(request):
    if request.method=='POST':
        form=DetailsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=DetailsForm()
    return render(request,'index.html',{'form':form})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['password2'] 
        
        if password==repassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Incorrect password')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method=="POST":
        username= request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Credentials did not match')
            return redirect('login')
    return render(request,'login.html')

def contact(request):
    if request.method=='POST':
        form=ContactInfoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ContactInfoForm()
    return render(request,'contact.html',{'form':form})

def reserve(request):
    if request.method=='POST':
        form=ReserveInfoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ReserveInfoForm()
    return render(request,'reserve.html',{'form':form})

def cancel(request):
    pass
