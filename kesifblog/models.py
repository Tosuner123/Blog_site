from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from slugify import slugify
from django.utils.text import slugify
from django import forms

CATEGORY_CHOICES = (
    ('Yazılım', 'Yazılım'),
    ('Kitap', 'Kitap'),
    ('Film/Dizi', 'Film/Dizi'),
    ('Spor', 'Spor'),
    ('Oyun', 'Oyun'),
    ('Felsefe', 'Felsefe'),
    ('Psikoloji', 'Psikoloji'),
    ('Tarih', 'Tarih'),
)
CATEGORY_IMAGE = (
    ('Software', 'Software'),
    ('Book', 'Book'),
    ('Movie', 'Movie'),
    ('Football', 'Football'),
    ('Game', 'Game'),
    ('Philosophy', 'Philosophy'),
    ('Psychology', 'Psychology'),
    ('History', 'History'),
)
class Blog_Content(models.Model):

    baslik = models.CharField(max_length=200)
    icerik = RichTextUploadingField(blank=True, null=True)
    kategori = models.CharField(max_length=100, choices=CATEGORY_CHOICES) 
    kategori_image = models.CharField(max_length=100, choices=CATEGORY_IMAGE) 
    created_date = models.DateField(auto_now_add=True)
    yazar = models.CharField(max_length=200)  
    icerik_info = models.TextField(blank=False, null=False,default='default')
    image = models.ImageField(upload_to='img', blank=True, null=True)
    card_image = models.ImageField(upload_to='img', blank=True, null=True)
    yeni_eklendi = models.BooleanField(default=False)
    onerilenler = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile', blank=True, null=True)

    # slug = models.SlugField(unique=True, allow_unicode=True, default="")

    # def save(self, *args, **kwargs):
        
    #     if not self.slug:
    #         self.slug = slugify(self.baslik)
    #     super(Blog_Content, self).save(*args, **kwargs)
    

    

    def __str__(self):
        return self.baslik

from django.db import models

class FooterInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


# class Blog_Card(models.Model):
#     baslik = models.CharField(max_length=200)
#     icerik_info = models.TextField(blank=False, null=False)
#     kategori = models.CharField(max_length=100, choices=CATEGORY_CHOICES) 
#     created_date = models.DateField(auto_now_add=True)
#     yazar = models.CharField(max_length=200)

#     def __str__(self):
#         return self.baslik
