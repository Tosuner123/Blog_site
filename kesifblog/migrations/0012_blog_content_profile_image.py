# Generated by Django 4.1.3 on 2023-10-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kesifblog', '0011_blog_content_yeni_eklendi'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_content',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
