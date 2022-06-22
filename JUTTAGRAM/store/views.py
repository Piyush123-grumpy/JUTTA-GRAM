from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import Category, Product


# Create your views here.
def home(request):
    return render(request,'home.html/')

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, 'collections.html',context)

def collectionView(request, slug):
    if Category.objects.filter(slug=slug, status=0):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products':products, 'category':category}
        return render(request,'product/index.html', context)
    else:
        messages.warning(request, "no such model found")
        return redirect('collections')


def productview(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products':products}
            
        else:
            messages.warning(request, "no such product found")
            return redirect('collections')
    else:
        messages.warning(request, "no such category found")
        return redirect('collections')
    return render(request, 'product/view.html',context)