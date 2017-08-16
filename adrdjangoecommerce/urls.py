from django.conf.urls import url, include
from django.contrib import admin
from core import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
#    url(r'^registro/$', views.RegisterView.as_view(), name='register'),
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^compras/', include('checkout.urls', namespace='checkout')),
    url(r'^admin/', admin.site.urls),
]
