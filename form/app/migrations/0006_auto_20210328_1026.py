# Generated by Django 3.0.1 on 2021-03-28 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210328_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signnow',
            name='label',
        ),
        migrations.RemoveField(
            model_name='signnow',
            name='types',
        ),
    ]
