# Generated by Django 3.1.7 on 2021-03-30 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210330_0537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signnow',
            name='page_number_t',
        ),
        migrations.RemoveField(
            model_name='signnow',
            name='x_t',
        ),
        migrations.RemoveField(
            model_name='signnow',
            name='y_t',
        ),
    ]