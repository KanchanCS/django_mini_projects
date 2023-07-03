from django.shortcuts import render,redirect
from .models import Bookmarks
import django_filters
from django import forms
# from .forms import EditForm
# Create your views here.
def index(request):
    books = Bookmarks.objects.all()
    return render(request,"filter.html",{"books":books}) 

class Bookmarksfillter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        label="Title",
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    
    class Meta:
        model = Bookmarks
        fields = [ 
            "title"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        ]

def index(request):
    filter = Bookmarksfillter(
        request.GET, queryset=Bookmarks.objects.all()
    )
    return render(
        request,
        "filter.html",
        {"filter": filter},
    )  

# def edit(request):
#     if request.method == 'POST':
#         form = EditForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('view-profile')
#     else:
#         form = EditForm(instance=request.user)

#     return render(request ,'edit-profile.html', {'form':form} )