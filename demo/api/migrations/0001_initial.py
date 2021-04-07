# Generated by Django 3.1.7 on 2021-04-07 16:10

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faxnumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('fax_file', models.FileField(upload_to='faxed/')),
            ],
        ),
        migrations.CreateModel(
            name='htmlformsign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('mobilenum', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='upload/')),
                ('text', models.CharField(max_length=200)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('page_no', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
    ]
