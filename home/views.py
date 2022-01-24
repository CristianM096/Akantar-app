from django.shortcuts import render
# Create your views here.

def home_view(request):
    return render(request,'home/index.html')

def page_view(request):
    return render(request,'home/page1.html')
