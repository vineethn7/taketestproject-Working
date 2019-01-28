from django.shortcuts import render


def post(request):
    return render(request, 'TakeTestApp/post.html', {'title': 'Post Test'})


def home(request):
    return render(request, 'TakeTestApp/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'TakeTestApp/about.html')
