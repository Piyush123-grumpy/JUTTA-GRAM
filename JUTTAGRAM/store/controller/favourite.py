from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from store.models import Favo, Product

@login_required(login_url='loginpage')
def index(request):
    favourite = Favo.objects.filter(user=request.user)
    context = {'favourite':favourite}
    return render(request,'favourite.html',context)

def addtofav(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Favo.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':"Product already in favourite"})
                else:
                    Favo.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Porduct added to favourite"})
            else: 
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"login to continue"})
    return redirect('/')