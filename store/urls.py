from django.urls import path

from store import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('contact-form/', views.contact_form_submit, name="contact_form"),
    path('newsletter/', views.newsletter_form_submit, name="newsletter_form"),
    path('booking/<str:car_id>/', views.booking, name="booking"),
    path('fleet/', views.fleet, name="fleet"),
    path('offers/', views.offers, name="offers"),
]