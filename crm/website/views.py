from django.shortcuts import render,HttpResponse
def home(request):
    return render(request,'index.html')
    # return HttpResponse('this is home page')
def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html')

def customer(request):
    return HttpResponse("this is customer page") 
# Create your views here.
