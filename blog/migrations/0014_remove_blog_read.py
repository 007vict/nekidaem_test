# Generated by Django 2.2.4 on 2019-09-26 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_blog_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='read',
        ),
    ]
