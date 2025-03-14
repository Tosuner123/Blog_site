# Generated by Django 4.2.6 on 2023-10-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('icerik', models.TextField(default='İçerik')),
                ('kategori', models.CharField(choices=[('Yazılım', 'Yazılım'), ('Kitap', 'Kitap'), ('Film/Dizi', 'Film/Dizi'), ('Spor', 'Spor')], max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('yazar', models.CharField(max_length=200)),
                ('icerik_info', models.TextField(default='default')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('card_image', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
        ),
    ]
