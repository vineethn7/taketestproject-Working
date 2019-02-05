from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

USER_TYPE_CHOICES = (
    ('student', 'Student'),
    ('organization', 'Organization'),
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    user_type = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','user_type']
