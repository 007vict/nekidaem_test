# Generated by Django 2.2.4 on 2019-08-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190821_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]