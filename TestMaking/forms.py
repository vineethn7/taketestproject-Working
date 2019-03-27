from django import forms
from .models import QuesModel


file1 = open('media/Test/TestName/ques.txt', 'r')
lines = file1.readlines()
file1.close()
ques = []
options = []
ans = []
for line in lines:
    if "Q:" in line:
        ques.append(line)
    if "opt" in line:
        options.append(line.replace('*', ''))
    if "*" in line:
        ans.append(line)
i = 0
quesBank = {}
for qu in ques:
    quesBank[qu] = [options[x] for x in range(i, i + 4)]
    i = i + 4
# Create your models here.

class QuesForm(forms.ModelForm):

    option = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices = options)
    class Meta:
        model = QuesModel
        fields = ['ques', 'option']
