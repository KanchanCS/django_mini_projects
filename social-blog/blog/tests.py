from django.test import TestCase
from django.shortcuts import render

# Create your tests here.
def home(request):
    return render(request, "home.html")
