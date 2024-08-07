# Generated by Django 5.0.6 on 2024-06-28 15:32

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='houses')),
                ('description', tinymce.models.HTMLField()),
                ('keywords', models.CharField(max_length=300, null=True)),
                ('seo_description', models.TextField(null=True)),
            ],
        ),
    ]
