from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    # path('elements/', views.elements, name='elements'),
    # path('blog/', views.blog, name='blog'),
    # path('blog/details/', views.blog_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('apply/', views.apply, name='apply'),

]