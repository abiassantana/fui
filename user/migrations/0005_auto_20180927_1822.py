# Generated by Django 2.1 on 2018-09-27 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20180927_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_animal',
            name='photo',
            field=models.ImageField(null=True, upload_to='clients_photos/'),
        ),
    ]
