from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('detail_page/', views.detail_page, name='detail_page'),
    path('listing_page/', views.listing_page, name='listing_page'),
]