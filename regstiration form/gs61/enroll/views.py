# Create your views here.
from .forms import SignUpForm
from django.shortcuts import render
# from django.contrib import messages


def sign_up(request):
    if request.method == 'post':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            # messages.success(request, 'Account Created Successfully')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': fm})
