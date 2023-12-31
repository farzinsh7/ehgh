# Generated by Django 4.2.4 on 2023-10-03 13:40

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('about', ckeditor_uploader.fields.RichTextUploadingField()),
                ('mission', ckeditor_uploader.fields.RichTextUploadingField()),
                ('quote', ckeditor_uploader.fields.RichTextUploadingField()),
                ('sub_industries', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='SiteInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('logo', models.ImageField(null=True, upload_to='logo')),
                ('description', models.TextField(null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=120, null=True)),
                ('icon', models.CharField(max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('main_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='socials', to='home.siteinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='slider')),
                ('home_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sliders', to='home.homedata')),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('home_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='features', to='home.homedata')),
            ],
        ),
    ]
