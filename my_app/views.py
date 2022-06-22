from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic

from my_app.form import UserRegistrationForm


def registerView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)   #
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST['email']
        print(username)
        password = request.POST['pass']
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            form = AuthenticationForm()
            return render(request, 'index.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'index.html', {'form': form})


def homeview(request):
    return HttpResponse("successfully logged in !!!")


def books(request):
    if request.user.is_authenticated:
        return render(request, 'blog.html')
    else:
        return redirect('login')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"
