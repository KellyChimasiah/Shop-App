from django.urls import path
from shop import views

urlpatterns=[
    path('',views.shop,name='home'),
    path('about/<int:item_id>/', views.about,name='about'),
    path('contact/',views.contact, name='contact')
  
]