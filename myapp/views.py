from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def shop(request):
    return render(request,'shop.html')


def about(request):
    return render(request,'about.html')