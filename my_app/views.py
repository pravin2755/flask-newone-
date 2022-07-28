import uuid
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import generic, View
from my_app.form import UserRegistrationForm, BlogForm
from my_app.models import Blog, PasswordChange
import logging
import sys
from my_project.settings import urls

logger = logging.getLogger()

loggers = {}
FORMATTER = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(FORMATTER)
logger.addHandler(console_handler)


file_handler = logging.FileHandler("test.log", "a", "utf8")
file_handler.setFormatter(FORMATTER)
logger.addHandler(file_handler)
logger.propagate = False
loggers["test"] = logger



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
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # user authorized or not, check here !!!
        if user is not None:  # checked user none or not !!!
            login(request, user)
            print(request.user.username)
            logger.info("User {} is logged in.".format(username))
            return redirect('/')
        else:
            form = AuthenticationForm()
            logger.error("User {} credential id not corrected.".format(username))
            return render(request, 'index.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'index.html', {'form': form})


"""
    logout function for log out !!!
"""


def logout_view(request):
    user=request.user.username
    logout(request)
    logger.info("User {} is logged out.".format(user))
    return redirect('login')


def home(request):
    user_check = False
    all_blog = Blog.objects.all().values()
    user_name = request.user.username
    if request.user.is_authenticated:
        user_check = True
        all_blog = Blog.objects.all().values()
        for i in all_blog:
            u_id = i['user_id']
            u_insta = User.objects.get(id=u_id)
            i['user_id'] = u_insta
            # logger.info("User {} is logged in.".format(user_name))
    return render(request, 'homepage.html',
                  {"all_blog": all_blog, "check_eligibility": user_check, "user_name": user_name})

    # user_name = ''  # global variable defined
    # user_check = False
    # all_blog = Blog.objects.all().values()   # blog details get
    # print(all_blog)
    # c=Blog.objects.filter("user_id")
    # print(c)
    # user_check = True
    # return render(request, 'homepage.html',
    #               {"check_eligibility": user_check, "user_name": user_name, "all_blog": all_blog})


def blog(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        user_blog = User.objects.filter(username=request.user.username)

        logger.info("User {} get their blog .".format(user_name))
        return render(request, 'blog.html')
    else:
        return redirect('login')


def about(request):
    user_name=request.user.username
    logger.info("User {} is entered in about page.".format(user_name))
    return render(request, 'about.html')


'''
    create registration page using class based view.
    this function taken data from the frontend and those data stored in to database.
'''


# class SignUpView(generic.CreateView):
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy("login")
#     template_name = "register.html"


'''
    Below function based view of registration without using form.
    this functon taken request from the frontend side and  stored data of user  to the database!!!
'''


# def signup(request):
#     if request.method == 'POST':
#
#         username = request.POST['username']
#         username = request.POST.get('username')
#         email = request.POST['email']
#         firstname = request.POST['first_name']
#         lastname = request.POST['last_name']
#         password = request.POST['password1']
#         confirm_password = request.POST['password2']
#         if password == confirm_password:
#             user = User.objects.create_user(username=username,  # create user in database.
#                                             email=email,
#                                             first_name=firstname,
#                                             last_name=lastname,
#                                             password=password,
#                                             )
#
#             user.save()
#             return redirect('login')
#
#     else:
#         return render(request, 'register.html')


#
# def blog_details(request, render_to_response=None):
#     if request.method == "POST" and request.user.is_authenticated:
#         blog_data = Blog.objects.all()
#         context = {"blog_data": blog_data}
#         return render(request, 'blog.html', context)


# class Blog(generic.ListView):
#     def get(self, request, *args, **kwargs):
#
#         return {"Status": True}
#
#     def post(self, request, *args, **kwargs):
#         return {"Status": True}


class MyFormView(View):
    temp_blog = 'blog.html'

    def get(self, request, *args, **kwargs):
        user_name = request.user.username
        if request.user.is_authenticated:
            user_blog1 = User.objects.filter(username=request.user.username).values("id")
            ghg = Blog.objects.filter(user_id=user_blog1[0]["id"]).values()
            initial = {'blog_data': ghg, "user_name": user_name}  # always iteration perform on key not objects.
            logger.info("User {} get their blog successfully.".format(user_name))
            return render(request, self.temp_blog, initial)
        else:
            return redirect("login")

#
# class MONGLiDH(View):
#     def post(self, request, *args, **kwargs):
#         try:
#             title = request.POST.get('title')
#             blog_dis = request.POST.get('blog_dis')
#             choice = request.POST.get('choice')
#             date_detail = request.POST.get('title')
#             images_upload = request.POST.get('title')
#             blog = Blog.objects.create(title=title,
#                                        blog_dis=blog_dis,
#                                        choice=choice,
#                                        date_detail=date_detail,
#                                        images_upload=images_upload,
#                                        )
#             abc = Blog(title="title",
#                        blog_dis="blog_dis",
#                        choice=1)
#             abc.save()
#             # logger.info("User {} is try to change password using email  .".format(username))
#             return {'success': True, 'status': 200}
#         except Exception:
#             return {'success': False, 'status': 400}


def blog_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.user

            title = request.POST['title']
            # username = request.POST.get('title')
            blog_dis = request.POST['blog_dis']
            choice = request.POST['choice']
            images_upload = request.FILES['images_upload']

            if request.user.is_authenticated:
                user = Blog.objects.create(user=username,
                                           title=title,  # create user in database.
                                           blog_dis=blog_dis,
                                           choice=choice,
                                           images_upload=images_upload,

                                           )
                logger.info("User {}  has been created blog successfully .".format(username))
    return render(request, 'addblog.html', {'blogform': BlogForm})


def forgot_password(request):
    if request.method == 'POST':
        username = request.POST['email']
        user1 = User.objects.filter(email=username)
        uid = user1[0].id
        print(uid)
        if user1 is not None:
            abc = str(uuid.uuid4().hex)
            print(PasswordChange.objects.filter(userpass=uid))
            if PasswordChange.objects.filter(userpass=uid):

                PasswordChange.objects.filter(userpass=uid).update(sluggs=abc)
            else:
                PasswordChange.objects.create(userpass=user1[0], sluggs=abc)
            logger.info("User {} is try to change password using email  .".format(username))
            return redirect(urls+'change/' + abc + "/")
    else:
        return render(request, "forget.html")


class PassChange(View):
    def get(self, request, slug):
        return render(request, "reset_pass.html")

    def post(self, request, slug):
        pas = PasswordChange.objects.get(sluggs=slug)
        passid = pas.userpass
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        print(pass1, pass2)
        if pass1 == pass2:
            encryptedpassword = make_password(pass1)
            print(encryptedpassword)
            checkpassword = check_password(pass1, encryptedpassword)
            print(checkpassword)
            usr = User.objects.filter(id=passid.id).update(password=encryptedpassword)
            logger.info("User {} password  is changed successfully  .".format(passid))
            return redirect("login")


# def checking(request):
#     return render(request, "child.html")
