from django.urls import path
from . import views

from store.controller import authview, cart, favourite
 
urlpatterns = [
    
    path('', views.home, name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>/',views.collectionView,name="collectionView"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),

    path('register/',authview.register,name="register"),
    path('login/',authview.loginpage,name="loginpage"),
    path('logout/',authview.logoutpage,name="logoutpage"),

      path('add-to-cart',cart.addtocart,name="addtocart"),

    path('cart/',cart.viewcart,name="cart"),

    path('favourite',favourite.index,name="favourite"),
    path("add-to-fav",favourite.addtofav, name="addtofav")
]