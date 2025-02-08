from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'), #To welcome Page
    path('login/', views.login_user, name='login'), #login page
    path('index/', views.index, name='index'),  #after login go to index page
    path('register/', views.register_user, name='register'),    #new user registration
    path('logout/', views.logout_user, name='logout'),  #loging out
    path('product_l/', views.product_l, name='product_l'),  #view the products
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),   #add to cart=>iew cart
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),   #remove items from cart
    path('cart_l/', views.cart_l, name='cart_l'),   #view cart
]