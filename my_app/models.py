from django.db import models


class Register(models.Model):
    username = models.EmailField(unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    password = models.CharField(max_length=50)
    Confirm_password = models.CharField(max_length=50)



class Blog(models.Model):
    login = models.ForeignKey(Register,related_name='log', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    blog = models.TextField(max_length=250)





