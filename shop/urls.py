
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='shopindex'),
    path('about',views.aboutus,name='aboutus'),
    path('contact',views.contactus,name='contactus'),
    path('productview/<int:pid>',views.productview,name='proview'),
    path('checkout/',views.checkout,name='checkout'),
    path('search/',views.search,name='search'),
]
