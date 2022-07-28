from django.contrib.auth.models import User
from django.db import models




class Blog(models.Model):
    CHOICES_select = (
        ("1", "One"),
        ("2", "Two"),
        ("3", "Three"),
        ("4", "Four"),
        ("5", "Five"),
    )

    user = models.ForeignKey(User,related_name='user1', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    blog_dis = models.TextField(max_length=250, null=True, blank=True)
    choice = models.CharField(choices=CHOICES_select, max_length=10, default=1)
    date_detail = models.DateTimeField(auto_now=True)
    images_upload = models.ImageField(upload_to="upload/")


class PasswordChange(models.Model):
    userpass= models.ForeignKey(User,related_name='user2', on_delete=models.CASCADE,default=0
                                )
    sluggs = models.CharField(max_length=255,null=True, blank=True)






