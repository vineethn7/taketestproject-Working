from django.shortcuts import render


def home(request):
    return render(request, 'TakeTestApp/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'TakeTestApp/about.html', {'title' : 'About'})
