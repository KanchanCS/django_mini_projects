from django import forms

from .models import BankRegistration, Choice


class BankRegistrationForm(forms.ModelForm):
    CHOICES = Choice.GENDER
    gender = forms.CharField(
        label='Choose Gender', widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = BankRegistration
        fields = ['first_name', 'last_name', 'age', 'mobile',
                  'email', 'gender', 'hobbies', 'bank', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(BankRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
