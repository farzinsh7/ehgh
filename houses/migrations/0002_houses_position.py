# Generated by Django 5.0.6 on 2024-06-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='position',
            field=models.IntegerField(null=True),
        ),
    ]