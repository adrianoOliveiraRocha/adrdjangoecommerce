# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^carrinho/adicionar/(?P<slug>[\w_-]+)/', views.CreateCartItemView.as_view(),
        name='create_cart_item'),
    url(r'^carrinho/$', views.CartItemView.as_view(), name='cart_item'),
    url(r'^finalizando/$', views.CheckoutView.as_view(), name='checkout')
]

