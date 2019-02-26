from django import forms


class TestFORM(forms.Form):
    CHOICES = (('a', 'A'),
               ('b', 'B'),
               ('c', 'C'),
               ('d', 'D'))
    options = forms.MultipleChoiceField(label=False, choices=CHOICES, widget=forms.RadioSelect())
