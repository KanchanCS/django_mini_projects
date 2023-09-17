from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

# from django.contrib.auth.decorators import login_required
from .forms import LoginForm, PostForm, RegisterForm
from .models import Category, Post

# Create your views here.
def Home(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{'posts':posts})

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("blog:login")
    else:
        form = RegisterForm()
       
    context = {
        "form": form,
    }
    return render(request, "signup.html", context)

def Login(request):
   
        if request.method == "POST":
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return redirect("blog:home")
                    
        else:
            form = LoginForm()

        context = {"forms": form}
        return render(request, "login.html", context)

def Logout(request):
    logout(request)
    return redirect("blog:home")

def blog_detail(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=id)
        context = {"post": post}
        return render(request, 'details.html', context)
    else:
        return redirect('blog:login')

# add New Post
def add_post(request):
        if request.method == 'POST':
            
            form = PostForm(request.POST, request.FILES)  
            if form.is_valid():
                author = request.user
                image = form.cleaned_data['image']
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                category_names = form.cleaned_data['category']  # Assuming category is a multiple select field
                post = Post(author=author, image=image, title=title, content=content)
                post.save()  # Save the post instance first

                for category_name in category_names:
                    category = get_object_or_404(Category, name=category_name)
                    post.category.add(category)  # Add categories to the post

                form = PostForm()  # Clear the form
                return redirect("blog:home")
        else:
            form = PostForm()
        return render(request, 'create_post.html', {'form': form})
   
    
# Edit Post
def edit_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)        
        return render(request, 'edit_post.html', {'form':form})
    else:
        return redirect("blog:login")  

# Delete Post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return redirect('blog:home')
    else:
        return redirect("blog:login")         

#filter

