# Generated by Django 2.2.4 on 2019-09-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_blog_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='read',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
