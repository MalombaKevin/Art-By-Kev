# Generated by Django 3.2.1 on 2022-05-29 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artgallery', '0005_alter_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_url',
        ),
    ]