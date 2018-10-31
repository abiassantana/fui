# Generated by Django 2.1.1 on 2018-10-30 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20181025_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='note',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user_rater',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
