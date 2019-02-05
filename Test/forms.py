from django import forms
from .models import TestM


class TestForm(forms.ModelForm):
    class Meta:
        model = TestM
        fields = ['TestName', 'MaxMarks', 'TimeDuration', 'PosMarks', 'NegMarks', 'InputTextFile']
