import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_item(request, id):
    item = Item.objects.get(id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': item.name},
                'unit_amount': item.price,  # Убедись, что price в центах!
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return JsonResponse({'session_id': session.id})

def item_page(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'item.html', {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })

def success_page(request):
    return render(request, 'success.html')

def cancel_page(request):
    return render(request, 'cancel.html')
