from django.shortcuts import render,HttpResponse, HttpResponse, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have successfully logined")
            return redirect('home')
        else:
            messages.success(request, "there is some error")
            return redirect('home')
    else:
        return render(request,'index.html')
    # return HttpResponse('this is home page')
def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html')

def customer(request):
    return HttpResponse("this is customer page")
def login_user(request):
    pass
def logout_user(request):
    logout(request)
    messages.success(request, "You hanve succrssfully loged out")
    return redirect('home')