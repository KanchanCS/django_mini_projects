from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.template.defaultfilters import filesizeformat

from .models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["name", "caption", "upload_file", "content"]

    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
