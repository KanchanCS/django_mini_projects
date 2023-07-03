from django.shortcuts import render, redirect
from .models import Feedback
# Create your views here.

def feedback(request):
    if request.method=="POST":
        username=request.POST.get("un")
        print(username)
        rate=request.POST.get('r')
        print(rate)
        msg=request.POST.get('msg')
        print(msg)
        Feedback.objects.create(username=username,rating=rate,feed_data=msg)
        data=Feedback.objects.all()
        context={'data':data}
        return render(request,'feedback.html', context)
    else:
        data=Feedback.objects.all()
        context={'data':data}
        return render(request,'feedback.html', context)

