from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Post



class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    required_css_class = "required"

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"    
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['image','title', 'content', 'category']


        
      
        
        





    


