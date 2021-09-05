from django.shortcuts import render, redirect
from .registerForm import NewUserForm
from django.contrib.auth import login as auth_login

from django.contrib.auth import authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

#Register New User
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Regestration Successful")
            return redirect("CustomerLogin:customerDashboard")
        messages.error(request, "Unsuccessful regestration. Invalid Information.")
    form = NewUserForm()
    return render(request, 'CustomerLogin/register.html',{'register_form':form})
# Login View
def login(request):
    if(request.method=='POST'):
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                auth_login(request, user)
                #messages.info(request, f'Your are now logged in {username}.')
                return redirect("CustomerLogin:customerDashboard")
            else:
                messages.error(request, "Invalid  username of password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, 'CustomerLogin/login.html',{"login_form":form})
# Logout
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("CustomerLogin:customerLogin")

# Dashboard view 
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("CustomerLogin:customerLogin")
    else:
        return render(request, 'CustomerLogin/dashboard.html')