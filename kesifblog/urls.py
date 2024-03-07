from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('anasayfa/', views.index, name='index'), 
    path('yazılım/', views.software, name='software'), 
    path('oyun/', views.game, name='game'), 
    path('felsefe/', views.philos, name='philos'), 
    path('tarih/', views.history, name='history'), 
    
    path('home/', views.handle_footer_form, name='footer_info'),
    path('spor/', views.spor, name='spor'),
     
    path('kitap/',views.book, name='book'),
    path('film-dizi/',views.movie_series, name='movie_series'),
]
    

    

