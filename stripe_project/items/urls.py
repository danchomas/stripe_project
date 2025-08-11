from django.urls import path
from .views import (
    ItemRetrieveView,
    PaymentInitiateView,
)

urlpatterns = [
    path('buy/<int:id>/', PaymentInitiateView.as_view(), name='buy_item'),
    path('item/<int:id>/', ItemRetrieveView.as_view(), name='item_page'),
]
