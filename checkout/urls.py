# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^carrinho/adicionar/(?P<slug>[\w_-]+)/',
        views.CreateCartItemView.as_view(), name='create_cart_item'),
    url(r'^carrinho/$', views.CartItemView.as_view(), name='cart_item'),
    url(r'^finalizando/$', views.CheckoutView.as_view(), name='checkout'),
    url(r'^finalizando/(?P<pk>\d+)/pagseguro/$', views.PagSeguroView.as_view(),
        name='pagseguro_view'),
    url(r'^finalizando/(?P<pk>\d+)/paypal/$', views.PaypalView.as_view(),
        name='paypal_view'),
    url(r'^meus-pedidos/$', views.OrderListView.as_view(), name='order_list'),
    url(r'^meus-pedidos/(?P<pk>\d+)$', views.OrderDetailView.as_view(),
        name='order_detail'),
    url(r'^notificacoes/pagseguro/$', views.pagseguro_notification,
        name='pagseguro_notification'),
]

