# Generated by Django 5.0.6 on 2024-06-29 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactus_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='image',
        ),
    ]
