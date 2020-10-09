from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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

def detail(request, question_id):
    return render(request, 'myweb/detail.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)