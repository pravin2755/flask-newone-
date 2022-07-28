from django.contrib import admin

from django.urls import path

from my_app.views import registerView, signin, home, blog, about, MyFormView, logout_view, \
    blog_add, forgot_password, PassChange

urlpatterns = [

    path('register/', registerView, name='register'),
    path('login/', signin, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('sign/', signup, name='sign'),
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('blog_add/', blog_add, name='blog_add'),
    path('about', about, name='about'),
    path('blog_details/', MyFormView.as_view(), name='blog_details'),
    # path('posthecck/', MONGLiDH.as_view(), name='MONGLiDH'),
    path('forget/', forgot_password, name='forget'),
    path("change/<str:slug>/",PassChange.as_view(),name="passchange"),
    # path('checking/',checking, name="checking")



]
