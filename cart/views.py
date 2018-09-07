from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """
    Renders the cart contents page
    """
    return render(request, "cart.html")

def add_to_cart(request, id):
    """
    Adds a quantity of the specified product to the cart
    """
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(reverse('index'))

def adjust_cart(request, id):
    """
    Adjusts quantity of the specified product to specified amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop[id]
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))