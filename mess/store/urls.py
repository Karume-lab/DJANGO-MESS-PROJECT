from django.urls import path
from . import views

urlpatterns = [
    path('', views.storeView, name = "store"),
    path('cart/', views.cartView, name = "cart"),
    path('checkout/', views.checkoutView, name = "checkout"),

    path('update_item/', views.updateItemView, name = "update_item"),
    path('process_order/', views.processOrderView, name = "rocess_order"),
]