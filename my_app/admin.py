from django.contrib import admin

from my_app.models import  Blog, PasswordChange

admin.site.register(Blog)
admin.site.register(PasswordChange)
