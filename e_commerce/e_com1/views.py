from django.shortcuts import render, redirect, get_object_or_404
from .models import Product,CartItem
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
  # Redirect to login page after logout
def signin(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or the home page
            return redirect('home')
        else:
            error_message = 'Invalid username or password'

            return render(request, 'index1.html', {'error_message': error_message})
    else:
        # If it's a GET request, render the login page
        return render(request, 'index1.html')
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('user_email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.save()

        messages.success(request, "Successfully created")
        
       
        return redirect('signin')

    return render(request, 'signup.html')



def home(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products': products})
    
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    # Calculate total cart amount
    total_cart_amount = sum(item.product.price * item.quantity for item in cart_items)
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_cart_amount': total_cart_amount})

def contact(request):
    return render(request,'contact.html')

def shop(request):
    products = Product.objects.all()

    # Configure the number of products per page
    paginator = Paginator(products, 12)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop.html', {'products': products})



def four(request):
    return render(request,'404.html')
def chackout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    # Calculate total cart amount
    total_cart_amount = sum(item.product.price * item.quantity for item in cart_items)
    total=total_cart_amount+15+20
    return render(request, 'chackout.html', {'cart_items': cart_items, 'total_cart_amount': total_cart_amount,'total': total})

def shopdetail(request):
    return render(request,'shop-detail.html')
def testimonial(request):
    return render(request,'testimonial.html')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Check if the product is already in the user's cart
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    
    if not created:
        # If the item already exists in the cart, increase the quantity by 1
        cart_item.quantity += 1
        cart_item.save()
    else:
        # Set quantity to 1 if it's a new item in the cart
        cart_item.quantity = 1
        cart_item.save()
    
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    
    # Delete the cart item
    cart_item.delete()

    return redirect('cart')

        

