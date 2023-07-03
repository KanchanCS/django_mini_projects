
import re

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import AccountCreationForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page
            return redirect('account:login')
            
    else:
        form = AccountCreationForm()
    return render(request, 'account/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        # validate email and password
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("account:home")
    else:
        form = LoginForm()
    context = {"form": form} 
    return render(request, "account/login.html", context)


def home(request):
    message =  "Your account has been login successful .." 
    return render(request, 'index.html', {'message': message}) 


# logout function
def logout_request(request):
    logout(request)
    return redirect("account:login")