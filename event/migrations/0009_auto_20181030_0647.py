# Generated by Django 2.1.1 on 2018-10-30 09:47

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20181025_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='event_logo/default.jpg', force_format=None, keep_meta=True, quality=0, size=[397, 397], upload_to='event_logo/'),
        ),
    ]
