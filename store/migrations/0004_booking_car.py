# Generated by Django 4.1.7 on 2023-03-07 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_offer_alter_booking_options_alter_car_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='store.car'),
        ),
    ]