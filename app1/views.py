from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login ,logout
from .models import Product,Cart,CartItem

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'home' with your desired home page URL
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})

def welcome(request):
    return render(request,'welcome.html')

def index(request):
    return render(request,'index.html', {'userName' : request.user.username})


from .forms import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with the name of your login URL pattern
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def logout_user(request):   #Logout user
    logout(request)
    return redirect('welcome')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(id=1)  # Example: Single cart instance for simplicity
    cart_item, created = CartItem.objects.get_or_create(product=product)
    cart_item.quantity += 0
    cart_item.save()
    cart.items.add(cart_item)
    return redirect('cart_l')

def remove_from_cart(request, item_id):   #Remove from cart
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_l')

def cart_l(request):
    cart, created = Cart.objects.get_or_create(id=1)  # Example: Single cart instance for simplicity
    return render(request, 'cart_l.html', {'cart': cart})

def product_l(request): 
    products = Product.objects.all()  # Fetch all products
    return render(request, 'product_l.html', {'products': products})


