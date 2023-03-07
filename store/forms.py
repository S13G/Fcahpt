from django import forms

from store.models import Newsletter, Contact, Booking


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            "pickup_date_and_time": forms.DateTimeInput(attrs={"name": "pickup_date_and_time"}),
            "return_date_and_time": forms.DateTimeInput(attrs={"name": "return_date_and_time"}),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})
