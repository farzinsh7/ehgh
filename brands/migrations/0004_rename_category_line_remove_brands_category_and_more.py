# Generated by Django 5.0.6 on 2024-06-08 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_category_tags_brands_category_brands_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Line',
        ),
        migrations.RemoveField(
            model_name='brands',
            name='category',
        ),
        migrations.RemoveField(
            model_name='brands',
            name='line',
        ),
    ]
