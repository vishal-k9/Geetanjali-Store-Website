"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth.views import login

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView



# from login.views import contact
from login.views import logout_page, signup
# from products.views import 
from website.views import admin_func, home_page
from carts.views import CartView, ItemCountView, CheckoutView, CheckoutFinalView
from orders.views import (
                    AddressSelectFormView, 
                    UserAddressCreateView, 
                    OrderList, 
                    OrderDetail)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin_func, name='admin'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^$', home_page, name='home') ,
    # url(r'^contact/$', contact , name='contact'),
    url(r'^orders/$', OrderList.as_view(), name='orders'),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^checkout/address/$', AddressSelectFormView.as_view(), name='order_address'),
    url(r'^checkout/address/add/$', UserAddressCreateView.as_view(), name='user_address_create'),
    url(r'^checkout/final/$', CheckoutFinalView.as_view(), name='checkout_final'),
    url(r'^logout/$', logout_page, name="logout_page"),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'), # If user is not login it will redirect to login page
    # url(r'^register/$', register, name="register"),
    # url(r'^register/success/$', register_success, name="register_success"),
    url(r'^signup/$', signup, name='signup'),
]
#matching urls to folders where they are
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

