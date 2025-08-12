import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentProcessor:
    @staticmethod
    def create_payment_session(item: Item) -> stripe.checkout.Session:
        return stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': item.name},
                    'unit_amount': int(item.price),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )


class ItemRetrieveView(views.APIView):
    @swagger_auto_schema(
        operation_description="Получение страницы товара",
        responses={
            200: openapi.Response('Успешный ответ', schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'item': openapi.Schema(type=openapi.TYPE_OBJECT),
                    'stripe_public_key': openapi.Schema(type=openapi.TYPE_STRING)
                }
            ))
        }
    )
    def get(self, request, id):
        item = self._get_item_or_404(id)
        return render(request, 'item.html', {
            'item': item,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        })

    @staticmethod
    def _get_item_or_404(item_id: int) -> Item:
        try:
            return Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            raise views.NotFound("Товар не найден")


class PaymentInitiateView(views.APIView):
    @swagger_auto_schema(
        operation_description="Создание платежной сессии",
        responses={
            200: openapi.Response('Успешный ответ', schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'session_id': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )),
            404: "Товар не найден"
        }
    )
    def get(self, request, id):
        item = self._get_item_or_404(id)
        session = PaymentProcessor.create_payment_session(item)
        return JsonResponse({'session_id': session.id})

    @staticmethod
    def _get_item_or_404(item_id: int) -> Item:
        try:
            return Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            raise views.NotFound("Товар не найден")


class PaymentSuccessView(views.APIView):
    @swagger_auto_schema(
        operation_description="Страница успешной оплаты",
        responses={200: "HTML страница"}
    )
    def get(self, request):
        return render(request, 'success.html')


class PaymentCancelView(views.APIView):
    @swagger_auto_schema(
        operation_description="Страница отмены оплаты",
        responses={200: "HTML страница"}
    )
    def get(self, request):
        return render(request, 'cancel.html')
