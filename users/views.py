from django.shortcuts import render, redirect
from .forms import RegistrationForm  # 9 import previous file forms
from django.contrib.auth import authenticate, login

# Create your views here.

# 6 create a view and then create a forms python file in users and import it here


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect('blog-name')

    else:
        form = RegistrationForm()

    context = {'form' : form}
    return render(request, 'register.html', context)
