# Generated by Django 5.0.6 on 2024-07-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_homedata_about_alter_homedata_about2'),
    ]

    operations = [
        migrations.AddField(
            model_name='homedata',
            name='header_img_mobile',
            field=models.ImageField(null=True, upload_to='home/header'),
        ),
        migrations.AddField(
            model_name='homedata',
            name='statistics_banner_mobile',
            field=models.ImageField(null=True, upload_to='home/banner'),
        ),
        migrations.AddField(
            model_name='homedata',
            name='video_banner_mobile',
            field=models.ImageField(null=True, upload_to='home/banner'),
        ),
    ]