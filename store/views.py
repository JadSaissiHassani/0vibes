from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, Product, DevlogEntry


def homepage(request):
    return render(request, 'store/homepage.html')


def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists.')
            return redirect('signup')

        user = CustomUser.objects.create_user(email=email, password=password)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'store/signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    return render(request, 'store/login.html')


def logout_view(request):
    logout(request)
    return redirect('homepage')


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'store/dashboard.html')


def products_view(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})


def customizer_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/customizer.html', {'product': product})

def devlog_view(request):
    entries = DevlogEntry.objects.all()
    return render(request, 'store/devlog.html', {'entries': entries})

def contact_view(request):
    return render(request, 'store/contact.html')


def policies_view(request):
    return render(request, 'store/policies.html')