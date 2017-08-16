from django.test import TestCase, Client
from model_mommy import mommy
from checkout.models import CartItem, Order
from django.core.urlresolvers import reverse
from django.conf import settings


class CartItemTestCase(TestCase):

    def setUp(self):
        mommy.make(CartItem, _quantity=3)

    def test_post_save_cart_item(self):
        cart_item = CartItem.objects.all()[0]
        cart_item.quantity = 0
        cart_item.save()
        self.assertEquals(CartItem.objects.count(), 2)



class CreateCartItemTestCase(TestCase):
    def setUp(self):
        self.product = mommy.make('catalog.Product')
        self.client = Client()
        self.url = reverse(
                'checkout:create_cart_item',
                kwargs={'slug': self.product.slug}
            )

    def tearDown(self):
        self.product.delete()
        CartItem.objects.all().delete()

    def test_add_cart_item_simple(self):
        response = self.client.get(self.url)
        redirect_url = reverse('checkout:cart_item')
        self.assertRedirects(response, redirect_url)
        self.assertEquals(CartItem.objects.count(), 1)

    def test_add_cart_item_complex(self):
        response = self.client.get(self.url)
        response = self.client.get(self.url)
        cart_item = CartItem.objects.get()
        self.assertEquals(cart_item.quantity, 2)


class OrderTestCase(TestCase):
    def setUp(self):
        self.cart_item = mommy.make(CartItem)
        self.user = mommy.make(settings.AUTH_USER_MODEL)

    def test_create_order(self):
        Order.objects.create_order(self.user, [self.cart_item])
        self.assertEquals(Order.objects.count(), 1)
        order = Order.objects.get()
        self.assertEquals(order.user, self.user)
        order_item = order.items.get()
        self.assertEquals(order_item.product, self.cart_item.product)
