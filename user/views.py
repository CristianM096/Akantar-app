from django.shortcuts import render

# Create your views here.

def user_view(request):
    return render(request,'user/index.html')

def landing_view(request):
    return render(request, 'user/landing.html')
