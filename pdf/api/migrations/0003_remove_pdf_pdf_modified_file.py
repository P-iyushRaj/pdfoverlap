# Generated by Django 3.1.7 on 2021-03-12 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_pdf_pdf_modified_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdf',
            name='pdf_modified_file',
        ),
    ]
