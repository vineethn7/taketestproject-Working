from django.shortcuts import render, redirect
from Test.models import TestM

# Create your views here.


def MakeTest(request):
    #file1 = open('media/Test/TestName/{}'.format(InputTextFile), 'r')
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
    return render(request, 'TestMaking/maketest.html', {'TestName': 'Test has begun', 'ques': ques, 'options': options, 'quesBank': quesBank})
