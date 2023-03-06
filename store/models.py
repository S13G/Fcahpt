from django.core.validators import MinValueValidator
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from common.models import BaseModel

# Create your models here.


TRANSMISSION_CHOICES = (
    ('A', 'Automatic'),
    ('M', 'Manual'),
)


class Car(BaseModel):
    name = models.CharField(max_length=255, null=True)
    image = ProcessedImageField(processors=[ResizeToFill(720, 480)], format='JPEG', options={'quality': 60}, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    passengers = models.IntegerField(validators=[MinValueValidator(1)])
    luggage = models.IntegerField(validators=[MinValueValidator(1)])
    doors = models.IntegerField(validators=[MinValueValidator(1)])
    transmission = models.CharField(max_length=1, choices=TRANSMISSION_CHOICES, default=None)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = None
        return url


class Newsletter(BaseModel):
    email = models.EmailField(max_length=300, null=True, unique=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.email}"


class Contact(BaseModel):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=300, null=True, unique=True)
    message = models.TextField(null=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} = {self.message}"


class Setting(BaseModel):
    website_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=100)
    company_email = models.EmailField()
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.website_name
