from django import forms
from .models import Bookmarks


class EditForm(forms.ModelForm):
    class Meta:
        model = Bookmarks
        fields = ('title','url', 'createdate')
    
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"         

class PostForm(forms.ModelForm):
    class Meta:
        model = Bookmarks
        fields = ('title')            