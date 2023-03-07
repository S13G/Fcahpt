import random

from django.contrib import messages
from django.shortcuts import render, redirect

from store.forms import NewsletterForm, ContactForm, BookingForm
from store.models import Car, Setting


# Create your views here.


def about(request):
    context = {"newsletter_form": NewsletterForm()}
    return render(request, 'store/about-us.html', context)


def booking(request):
    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            print(booking_form.errors)
            print(booking_form)
            messages.success(request, "You have successfully booked a car")
            return redirect('homepage')
        else:
            print(booking_form.errors)
            messages.info(request, "Error while booking")
    else:
        booking_form = BookingForm()
    cars = Car.objects.all()
    context = {"newsletter_form": NewsletterForm(), "cars": cars, "booking_form": booking_form}
    return render(request, 'store/fleet.html', context)


def contact(request):
    context = {"contact_form": ContactForm(), "newsletter_form": NewsletterForm()}
    return render(request, 'store/contact.html', context)


def home(request):
    cars = Car.objects.order_by("-id").all()
    settings = Setting.objects.all()
    count = min(cars.count(), 3)
    cars = random.sample(list(cars), count)
    context = {"cars": cars, "contact_form": ContactForm(), "newsletter_form": NewsletterForm(), "settings": settings}
    return render(request, 'index.html', context)


def contact_form_submit(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Form submitted successfully, we'll get back to you soon")
        else:
            messages.info(request, "Error submitting form")
    return redirect('homepage')


def newsletter_form_submit(request):
    if request.method == "POST":
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, "You have successfully signed up for the newsletter")
        else:
            messages.error(request, "Please provide a valid email address")
    return redirect('homepage')


def fleet(request):
    cars = Car.objects.all()
    context = {"newsletter_form": NewsletterForm(), "cars": cars, "booking_form": BookingForm()}
    return render(request, 'store/fleet.html', context)


def offers(request):
    cars = Car.objects.all()
    context = {"newsletter_form": NewsletterForm(), "cars": cars}
    return render(request, 'store/offers.html', context)
