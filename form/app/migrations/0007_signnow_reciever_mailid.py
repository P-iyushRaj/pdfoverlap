# Generated by Django 3.1.7 on 2021-03-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210328_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='signnow',
            name='reciever_mailid',
            field=models.EmailField(blank=True, max_length=2540, null=True),
        ),
    ]
