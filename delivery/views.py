from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Delivery
from .form import assignDeliveryForm, startDeliveryFrom
from django import forms


from .models import Delivery
from products.models import Producer

def start_delivery(request):
    if request.method == 'POST':
        form = startDeliveryFrom(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.sender = request.user

            producer = Producer.objects.get(brand_name = form.cleaned_data.get('brand_name'))

            producer.stock -= delivery.quantity
            producer.save()

            
            delivery.producer = producer

            delivery.save()
            messages.success(request, "Successfully placed order")
            return redirect("dashboard")
        else:
            messages.warning(request, "Something went wrong")
    else:
        form = startDeliveryFrom()

  
    brands = Producer.objects.values_list('brand_name', flat=True).distinct()
    form.fields['brand_name'] = forms.ChoiceField(choices=[(brand, brand) for brand in brands])

    context = {'form': form}
    return render(request, 'delivery/start_delivery.html', context)
    
def active_delivery(request):
    obj = Delivery.objects.filter(sender=request.user)
    context = {'obj':obj}
    return render(request,'delivery/active_delivery.html', context)
def delivery_history(request):
    obj = Delivery.objects.filter(sender=request.user)
    context = {'obj':obj}
    return render(request,'delivery/delivery_history.html', context)

#for wharehouse
def accept_delivery(request, serial_number):
    delivery = Delivery.objects.get(serial_number=serial_number)

    if request.method == 'POST':
        # Update only the is_accepted field
        delivery.is_accepted = True
        delivery.save()

        messages.success(request, "Delivery Accepted")
        return redirect('delivery-queue')
    else:
        return redirect('delivery-queue')


    

def delivery_queue(request):
    obj = Delivery.objects.filter(is_delivered=False)
    context = {'obj':obj}
    return render(request,'delivery/delivery_queue.html',context)


def reject_delivery(request, serial_number):
    delivery = Delivery.objects.get(serial_number=serial_number)

    if request.method == 'POST':
        delivery.is_rejected = True
        delivery.save()

        messages.success(request, "Delivery Rejected")
        return redirect('delivery-queue')
    else:
        context = {'obj': delivery}
        return render(request, 'delivery/reject_delivery.html', context)
