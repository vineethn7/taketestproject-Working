from django.shortcuts import render, redirect
from .forms import TestForm
from .models import TestM
# Create your views here.


def post(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return redirect('TakeTest-Home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()
    return render(request, 'Test/post.html', {'title': 'Test-post', 'form': form})
