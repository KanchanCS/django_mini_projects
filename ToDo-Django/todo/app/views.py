from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import AccountCreationForm, LoginForm


# Create your views here.
def home(request):
    message =  "Your account has been login successful .." 
    return render(request, 'home.html', {'message': message}) 
def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
             # Redirect to login page
            return redirect('app:login')
            
    else:
        form = AccountCreationForm()
    return render(request, 'register.html', {'form': form})


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
                return redirect("app:home")
    else:
        form = LoginForm()
    context = {"form": form} 
    return render(request, "login.html", context)

# logout function
def logout_request(request):
    logout(request)
    return redirect("login")

