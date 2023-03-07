from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from common.threads import EmailThread


class Util:
    @staticmethod
    def send_booking_receipt(booking):
        subject = "Booking Successful"
        car = booking.car  # get booked car instance
        message = render_to_string(
            "store/receipt.html",
            {"full_name": booking.full_name, "pickup_location": booking.pickup_location,
             "return_location": booking.return_location,
             "pickup_date_and_time": booking.pickup_date_and_time,
             "return_date_and_time": booking.return_date_and_time,
             "email_address": booking.email_address,
             "phone_number": booking.phone_number, "car_name": car.name}
        )
        email = EmailMessage(subject=subject, body=message, to=[booking.email_address])
        email.content_subtype = "html"
        EmailThread(email).start()
