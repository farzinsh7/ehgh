# Generated by Django 5.0.6 on 2024-06-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homedata_video_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='home/icons'),
        ),
    ]