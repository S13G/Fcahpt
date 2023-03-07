# Generated by Django 4.1.7 on 2023-03-06 20:15

from django.db import migrations, models
import store.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pickup_location', models.CharField(max_length=300)),
                ('pickup_date_and_time', models.DateTimeField()),
                ('return_location', models.CharField(max_length=300)),
                ('return_date_and_time', models.DateTimeField()),
                ('full_name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100, validators=[store.validators.validate_phone_number])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='setting',
            name='phone_number',
            field=models.CharField(max_length=100, validators=[store.validators.validate_phone_number]),
        ),
    ]
