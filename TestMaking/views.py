from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Choices

"""def SubmitTest(request):
    if request.method == 'POST':
        messages.success(request, 'Dear student, your test {} is submited successfully'.format(TestName))
        return redirect('profile')"""

@login_required
def MakeTest(request):
    #file1 = open('media/Test/TestName/{}'.format(InputTextFile), 'r')
    file1 = open('ques.txt', 'r')
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
    if request.method == 'POST':
        cleandata = self.cleaned_data['choices']
        messages.success(request, 'Dear student, your test {} is submited successfully'.format(TestName))
        return redirect('profile')
    context = {'TestName': 'Test has begun', 'ques': ques, 'options': options, 'quesBank': quesBank }
    return render(request, 'TestMaking/maketest.html', context)
