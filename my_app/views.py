from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic

from my_app.form import UserRegistrationForm

"""
using function based view   user registration data valid or not ,
if data is not valid then return error otherwise  stored it to the database
"""


def registerView(request):
    if request.method == 'POST':
        print(request)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
        else:
            print(form.errors)
    else:

        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


"""
using function based view  authenticate user for login,
if user authorized then user able to access data.
"""


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        password = request.POST['pass']
        print(password)
        user = authenticate(request, username=username, password=password)    # user authorized or not, check here !!!
        if user is not None:                                                   # checked user none or not !!!
            login(request, user)
            return redirect('/home')
        else:
            form = AuthenticationForm()
            return render(request, 'index.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'index.html', {'form': form})


"""
using function based view returned HttpResponse.
"""


def homeview(request):
    return HttpResponse("successfully logged in !!!")


def books(request):

    if request.user.is_authenticated:

        return render(request, 'blog.html')
    else:
        return redirect('login')


'''
    create registration page using class based view.
    this function taken data from the frontend and those data stored in to database.
'''


class SignUpView(generic.CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"


'''
    Below function based view of registration without using form.
    this functon taken request from the frontend side and  stored data of user  to the database!!!
'''


def signup(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        if password == confirm_password:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            first_name=firstname,
                                            last_name=lastname,
                                            password=password,
                                            )

            user.save()
            return redirect('login')

    else:
        return render(request, 'register.html')



