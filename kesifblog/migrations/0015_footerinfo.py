# Generated by Django 4.1.3 on 2023-10-27 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kesifblog', '0014_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('note', models.TextField()),
            ],
        ),
    ]
