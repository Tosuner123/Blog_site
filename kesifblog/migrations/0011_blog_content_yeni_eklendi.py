# Generated by Django 4.1.3 on 2023-10-22 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kesifblog', '0010_remove_blog_content_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_content',
            name='yeni_eklendi',
            field=models.BooleanField(default=False),
        ),
    ]
