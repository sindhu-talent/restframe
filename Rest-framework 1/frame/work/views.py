from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Test
from.forms import TestForm
from django.contrib.auth import authenticate,logout
def inner(request):
    return HttpResponse("computer")
def index(request):
    data=Test.objects.all()
    dict={"empdata":data}
    return render(request,'index.html',dict)
def create(request):
    if request.method=='POST':
        form=TestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/index/')
    else:
        form=TestForm()
    return render(request,'create.html',{'form':form})
def edit(request,name):
    empdata=Test.objects.get(name=name)
    form=TestForm(instance=empdata)
    return render(request,'Update.html',{'form':form,'name':name})
def delete(request,name):
    empdata=Test.objects.get(name=name)
    empdata.delete()
    return redirect('/index/')
def Update(request,name):
    empdata=Test.objects.get(name=name)
    form=TestForm(request.POST,instance=empdata)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    return render (request,'update.html',{'form':form,'name':name})
def login(request):
    if request.method=='POST':
        Uname=request.POST.get('Uname')
        pwd=request.POST.get('password')
        user=authenticate(username=Uname,password=pwd)
        if user:
            return redirect('/index/')
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return redirect('/login/')
def home(request):
    return render(request,'home.html')




# Create your views here.
