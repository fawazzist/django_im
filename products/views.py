from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producer
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.producer = request.user
            product.save()
            messages.success(request, "Product added successfully.")
            return redirect('products-dashboard')
        else:
            messages.error(request, "Invalid form data. Please check your inputs.")
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'products/register_products.html', context)



def product_list(request):
    products = Producer.objects.all()  

    context = {'products': products}
    return render(request, 'products/products_dashboard.html', context)

