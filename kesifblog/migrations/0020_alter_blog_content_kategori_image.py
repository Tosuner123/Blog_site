# Generated by Django 4.2.7 on 2023-11-20 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kesifblog', '0019_blog_content_kategori_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_content',
            name='kategori_image',
            field=models.CharField(choices=[('Software', 'Software'), ('Book', 'Book'), ('Movie', 'Movie'), ('Spor', 'Spor'), ('Game', 'Game'), ('Philosophy', 'Philosophy'), ('Psychology', 'Psychology'), ('History', 'History')], max_length=100),
        ),
    ]
