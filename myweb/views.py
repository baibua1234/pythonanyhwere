from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .form import addFood,addFoodType
from .models import FoodType , Food, Calorie

# Create your views here.
def index(req):
	return render(req, 'myweb/index.html')



def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    context['form']=form
    return render(request,'myweb/signup.html',context)

def logout(req):
    logout_user(req)
    return redirect('login')

def united(req):
	return render(req, 'myweb/united.html')

def savoryfood(req):
	return render(req, 'myweb/savoryfood.html')

def singledish(req):
	return render(req, 'myweb/singledish.html')

def snackfood(req):
	return render(req, 'myweb/snackfood.html')

def sweettreat(req):
    return render(req,'myweb/sweettreat.html')

#-----DATABASE------------------#

def showFood(req):
    food = Food.objects.all()
    return render(req ,'myweb/allfood.html' ,{'food':food})


def addFoodType(req):
    if req.method == "POST":
        form = addFoodType(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = addFoodType()
        context = {'form':form}
        return render(req, 'myweb/addfood.html',context)

def addfood(req):
    if req.method == "POST":
        form = addFood(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = addFood()
        context = {'form':form}
        return render(req, 'myweb/add.html',context)
