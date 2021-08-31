from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'BasicNavs/home.html')

def aboutUs(request):
    return render(request, 'BasicNavs/aboutUs.html')

def contactUs(request):
    return render(request, 'BasicNavs/contactUs.html')