from django import forms

from store.models import Newsletter, Contact, Booking, Car


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
    pickup_date_and_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
                                               label="Pick-up date/time")
    return_date_and_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
                                               label="Return date/time")
    car = forms.ModelChoiceField(queryset=Car.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Booking
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        car = kwargs.pop('car', None)
        super(BookingForm, self).__init__(*args, **kwargs)

        if car:
            self.fields['car'].initial = car.id

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})
