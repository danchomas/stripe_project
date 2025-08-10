from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:id>/', views.buy_item, name='buy_item'),
    path('item/<int:id>/', views.item_page, name='item_page'),
    path('cancel/', views.cancel_page, name='cancel_payment'),
    path('success/', views.success_page, name='success_payment'),
]
