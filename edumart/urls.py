from django.contrib import admin
from django.urls import path
import frontend.views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', v.index, name='index'),
    path('contact/', v.contact, name='contact'),
    path('cart/', v.cart, name='cart'),
    path('detail/<str:product_id>', v.detail, name='detail'),
    path('shop/', v.shop, name='shop'),  # All products
    path('shop_specific/<str:category>', v.shop_specific, name='shop_specific'),
    path('checkout/', v.checkout, name='checkout'),

]
