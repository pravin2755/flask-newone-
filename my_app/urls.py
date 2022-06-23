from django.contrib import admin

from django.urls import path

from my_app.views import registerView, homeview, signin, SignUpView, signup

urlpatterns = [

    path('register/', registerView, name='register'),
    path('login/', signin, name='login'),
    path('home/', homeview, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('sign/',signup, name='sign')

]
