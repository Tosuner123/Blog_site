# Generated by Django 4.1.3 on 2023-10-28 01:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kesifblog', '0015_footerinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='footerinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
