# Generated by Django 4.0.5 on 2022-07-01 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_blog_images_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='images_upload',
            field=models.ImageField(null=True, upload_to='upload_images/'),
        ),
    ]