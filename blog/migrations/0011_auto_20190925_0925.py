# Generated by Django 2.2.4 on 2019-09-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190925_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='read',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]