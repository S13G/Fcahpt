import random

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from common.email import Util
from store.forms import NewsletterForm, ContactForm, BookingForm
from store.models import Car, Setting, Offer


# Create your views here.


def about(request):
    context = {"newsletter_form": NewsletterForm()}
    return render(request, 'store/about-us.html', context)


def booking(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        booking_form = BookingForm(request.POST, car=car)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.car = car
            booking.save()
            messages.success(request, "Your booking was successful")

            Util.send_booking_receipt(booking)
            return redirect('homepage')
        else:
            messages.error(request, "Error with booking, try again")
    else:
        booking_form = BookingForm(initial={'car': car.id}, car=car)

    return render(request, 'store/booking.html', {'booking_form': booking_form, 'car': car})


def home(request):
    cars = Offer.objects.order_by("-id").all()
    settings = Setting.objects.all()
    count = min(cars.count(), 3)
    cars = random.sample(list(cars), count)
    context = {"cars": cars, "contact_form": ContactForm(), "newsletter_form": NewsletterForm(), "settings": settings}
    return render(request, 'index.html', context)


def contact(request):
    context = {"contact_form": ContactForm(), "newsletter_form": NewsletterForm()}
    return render(request, 'store/contact.html', context)


def contact_form_submit(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Form submitted successfully, we'll get back to you soon")
        else:
            messages.info(request, "Error submitting form")
    return redirect('homepage')


def fleet(request):
    cars = Car.objects.all()
    context = {"newsletter_form": NewsletterForm(), "cars": cars}
    return render(request, 'store/fleet.html', context)


def newsletter_form_submit(request):
    if request.method == "POST":
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, "You have successfully signed up for the newsletter")
        else:
            messages.error(request, "Please provide a valid email address")
    return redirect('homepage')


def offers(request):
    offers = Offer.objects.all()
    context = {"newsletter_form": NewsletterForm(), "offers": offers}
    return render(request, 'store/offers.html', context)
