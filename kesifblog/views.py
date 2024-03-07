from django.shortcuts import render,redirect, get_object_or_404
from .models import Blog_Content
from django.shortcuts import get_object_or_404
from .models import FooterInfo


def index(request,category = None):
   
    spor_icerikler = Blog_Content.objects.filter(kategori='Spor', yeni_eklendi=True).order_by('-created_date')[:1]


    yazilim_icerikler = Blog_Content.objects.filter(kategori='Yazılım', yeni_eklendi=True).order_by('-created_date')[:1]


    kitap_icerikler = Blog_Content.objects.filter(kategori='Kitap', yeni_eklendi=True).order_by('-created_date')[:1]
    
    oyun_icerikler = Blog_Content.objects.filter(kategori='Oyun', yeni_eklendi=True).order_by('-created_date')[:1]


    new_added = Blog_Content.objects.filter( yeni_eklendi=True).order_by('-created_date')[:3]


    if category:
        
        blogs = Blog_Content.objects.filter(kategori=category)
        
    else:
        
        blogs = Blog_Content.objects.all()

    context = {
        'blogs': blogs,
        'spor_icerikler': spor_icerikler,
        'yazilim_icerikler': yazilim_icerikler,
        'kitap_icerikler': kitap_icerikler,
        'oyun_icerikler': oyun_icerikler,
        'new_added': new_added,
    }   
    return render(request,'index.html',context)

def software(request):
    # spor_icerikler = Blog_Content.objects.filter(kategori='Spor', yeni_eklendi=True).order_by('-created_date')[:1]


    # yazilim_icerikler = Blog_Content.objects.filter(kategori='Yazılım', yeni_eklendi=True).order_by('-created_date')[:1]


    # kitap_icerikler = Blog_Content.objects.filter(kategori='Kitap', yeni_eklendi=True).order_by('-created_date')[:1]
    
    selected_category = "Yazılım" 
    blogs = Blog_Content.objects.order_by('-created_date')

    blogs = Blog_Content.objects.filter(kategori=selected_category)
    
    footer_blog = Blog_Content.objects.filter(kategori=selected_category, onerilenler=True).order_by('-created_date')[:4]

    context = {
        'blogs': blogs,
        # 'spor_icerikler': spor_icerikler,
        # 'yazilim_icerikler': yazilim_icerikler,
        # 'kitap_icerikler': kitap_icerikler,
        'footer_blog':  footer_blog,
    }
    return render(request, 'software.html', context)




# def blog_detail(request, blog_slug):
#     blog_post = get_object_or_404(Blog_Content, slug=blog_slug)
#     return render(request, 'software.html', {'blog_post': blog_post})




    
def spor(request,category="Spor"):
    spor_icerikler = Blog_Content.objects.filter(kategori='Spor').order_by('-created_date')[:1]


    yazilim_icerikler = Blog_Content.objects.filter(kategori='Yazılım', yeni_eklendi=True).order_by('-created_date')[:1]
    
    tum_icerikler = Blog_Content.objects.filter(yeni_eklendi=True).order_by('-created_date')

    kitap_icerikler = Blog_Content.objects.filter(kategori='Kitap', yeni_eklendi=True).order_by('-created_date')[:1]

    footer_blog = Blog_Content.objects.filter(kategori='Spor', onerilenler=True).order_by('-created_date')[:4]

    if category:
        
        blogs = Blog_Content.objects.filter(kategori=category)
    else:
        
        blogs = Blog_Content.objects.all()

    context = {
        'blogs': blogs,
        'spor_icerikler': spor_icerikler,
        'yazilim_icerikler': yazilim_icerikler,
        'kitap_icerikler': kitap_icerikler,
        'tum_icerikler': tum_icerikler,
        'footer_blog': footer_blog,
    }   
    return render(request,'spor.html',context) 


def book(request):
    spor_icerikler = Blog_Content.objects.filter(kategori='Spor', yeni_eklendi=True).order_by('-created_date')[:1]
    

    yazilim_icerikler = Blog_Content.objects.filter(kategori='Yazılım', yeni_eklendi=True).order_by('-created_date')[:1]


    kitap_icerikler = Blog_Content.objects.filter(kategori='Kitap', yeni_eklendi=True).order_by('-created_date')[:1]
   
    selected_category = "Kitap" 
    
    footer_blog = Blog_Content.objects.filter(kategori=selected_category, onerilenler=True).order_by('-created_date')[:4]

    
    blogs = Blog_Content.objects.filter(kategori=selected_category)

    context = { 
        'blogs': blogs,
        'spor_icerikler': spor_icerikler,
        'yazilim_icerikler': yazilim_icerikler,
        'kitap_icerikler': kitap_icerikler,
        'footer_blog': footer_blog,
    }
    return render(request, 'book.html', context)

def movie_series(request):
    spor_icerikler = Blog_Content.objects.filter(kategori='Spor', yeni_eklendi=True).order_by('-created_date')[:1]


    yazilim_icerikler = Blog_Content.objects.filter(kategori='Yazılım', yeni_eklendi=True).order_by('-created_date')[:1]


    kitap_icerikler = Blog_Content.objects.filter(kategori='Kitap', yeni_eklendi=True).order_by('-created_date')[:1]
     
    selected_category = "Film/Dizi"  
    
    footer_blog = Blog_Content.objects.filter(kategori=selected_category, onerilenler=True).order_by('-created_date')[:4]
    
    blogs = Blog_Content.objects.filter(kategori=selected_category)

    context = {
        'blogs': blogs,
        'spor_icerikler': spor_icerikler,
        'yazilim_icerikler': yazilim_icerikler,
        'kitap_icerikler': kitap_icerikler,
        'footer_blog': footer_blog,
    } 
    return render(request,'movie_series.html',context)
def game(request):
    spor_icerikler = Blog_Content.objects.filter(kategori='Spor', yeni_eklendi=True).order_by('-created_date')[:1]


    yazilim_icerikler = Blog_Content.objects.filter(kategori='Yazılım', yeni_eklendi=True).order_by('-created_date')[:1]


    kitap_icerikler = Blog_Content.objects.filter(kategori='Kitap', yeni_eklendi=True).order_by('-created_date')[:1]
    
    oyun_icerikler = Blog_Content.objects.filter(kategori='Oyun', yeni_eklendi=True).order_by('-created_date')[:1]
     
    selected_category = "Oyun"  
    
    footer_blog = Blog_Content.objects.filter(kategori=selected_category, onerilenler=True).order_by('-created_date')[:4]
    
    blogs = Blog_Content.objects.filter(kategori=selected_category)

    context = {
        'blogs': blogs,
        'spor_icerikler': spor_icerikler,
        'yazilim_icerikler': yazilim_icerikler,
        'kitap_icerikler': kitap_icerikler,
        'oyun_icerikler': oyun_icerikler,
        'footer_blog': footer_blog,
    } 
    return render(request,'game.html',context)
def philos(request):
    spor_icerikler = Blog_Content.objects.filter(kategori='Spor', yeni_eklendi=True).order_by('-created_date')[:1]


    yazilim_icerikler = Blog_Content.objects.filter(kategori='Yazılım', yeni_eklendi=True).order_by('-created_date')[:1]


    kitap_icerikler = Blog_Content.objects.filter(kategori='Kitap', yeni_eklendi=True).order_by('-created_date')[:1]
    
    oyun_icerikler = Blog_Content.objects.filter(kategori='Oyun', yeni_eklendi=True).order_by('-created_date')[:1]
     
    selected_category = "Felsefe"  
    
    footer_blog = Blog_Content.objects.filter(kategori=selected_category, onerilenler=True).order_by('-created_date')[:4]
    
    blogs = Blog_Content.objects.filter(kategori=selected_category)

    context = {
        'blogs': blogs,
        'spor_icerikler': spor_icerikler,
        'yazilim_icerikler': yazilim_icerikler,
        'kitap_icerikler': kitap_icerikler,
        'oyun_icerikler': oyun_icerikler,
        'footer_blog': footer_blog,
    } 
    return render(request,'philos.html',context)
def history(request):
    spor_icerikler = Blog_Content.objects.filter(kategori='Spor', yeni_eklendi=True).order_by('-created_date')[:1]


    yazilim_icerikler = Blog_Content.objects.filter(kategori='Yazılım', yeni_eklendi=True).order_by('-created_date')[:1]


    kitap_icerikler = Blog_Content.objects.filter(kategori='Kitap', yeni_eklendi=True).order_by('-created_date')[:1]
    
    oyun_icerikler = Blog_Content.objects.filter(kategori='Oyun', yeni_eklendi=True).order_by('-created_date')[:1]
     
    selected_category = "Tarih"  
    
    footer_blog = Blog_Content.objects.filter(kategori=selected_category, onerilenler=True).order_by('-created_date')[:4]
    
    blogs = Blog_Content.objects.filter(kategori=selected_category)

    context = {
        'blogs': blogs,
        'spor_icerikler': spor_icerikler,
        'yazilim_icerikler': yazilim_icerikler,
        'kitap_icerikler': kitap_icerikler,
        'oyun_icerikler': oyun_icerikler,
        'footer_blog': footer_blog,
    } 
    return render(request,'history.html',context)



def handle_footer_form(request):
   if request.method == 'POST':
       name = request.POST.get('name')  
       email = request.POST.get('email')
       note = request.POST.get('note')
       FooterInfo.objects.create(name=name, email=email, note=note)
       return redirect('index')  
   return redirect('index')

