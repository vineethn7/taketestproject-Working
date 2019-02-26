from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

USER_TYPE_CHOICES = (
    ('s', 'Student'),
    ('o', 'Organization'),
)

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    usertype = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=USER_TYPE_CHOICES)
    class Meta:
        model = User
        fields = ('username','password1', 'password2','email','usertype')
