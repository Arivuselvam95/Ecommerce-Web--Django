from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.signin, name='signin'),

    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'), 
    path('home', views.home, name='home'), 
    path('cart', views.cart, name='cart'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('four', views.four, name='four'),
    path('chackout', views.chackout, name='chackout'),
    path('shopdetail', views.shopdetail, name='shopdetail'),
    path('testimonial', views.testimonial, name='testimonial'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)