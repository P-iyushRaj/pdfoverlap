# Generated by Django 3.0.1 on 2021-03-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210328_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='signnow',
            name='doc_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
