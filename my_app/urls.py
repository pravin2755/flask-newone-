from django.contrib import admin

from django.urls import path

from my_app.views import registerView, homeview, signin, SignUpView

urlpatterns = [

    path('register/', registerView, name='register'),
    path('login/', signin, name='login'),
    path('', homeview, name='home'),
    path('cbase/', SignUpView.as_view(), name='signup')

]
