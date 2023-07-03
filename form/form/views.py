from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import BankRegistrationForm
from .models import BankRegistration

# Create your views here.


def register(request):

    if request.method == "POST":
        form = BankRegistrationForm(request.POST)
        if form.is_valid():

            send_mail(
                "Bank Register",
                "Your Registrations has been successfully.",
                "imkanchan7422@gmail.com",
                [form.cleaned_data["email"]],
                fail_silently=False,
            )
            form.save()
            return redirect("form:register")

    else:
        form = BankRegistrationForm()

    return render(request, "form.html", {"form": form})
