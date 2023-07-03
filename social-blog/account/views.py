from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:post")
    else:
        form = RegisterForm()

    context = {
        "form": form,
    }
    return render(request, "register.html", context)


def login_req(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:

                login(request, user)
                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
                else:
                    return redirect("blog:post")
    else:
        form = LoginForm()

    context = {"login_form": form}
    return render(request, "login.html", context)


def logout_request(request):
    logout(request)
    return redirect("account:login")
