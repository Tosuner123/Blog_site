# Generated by Django 4.1.3 on 2023-11-02 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kesifblog', '0016_footerinfo_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_content',
            name='onerilenler',
            field=models.BooleanField(default=False),
        ),
    ]
