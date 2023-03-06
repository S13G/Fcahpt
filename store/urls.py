from django.urls import path

from store import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('fleet/', views.fleet, name="fleet"),
    path('offers/', views.offers, name="offers"),
    path('testimonials,', views.testimonials, name="testimonials"),
]