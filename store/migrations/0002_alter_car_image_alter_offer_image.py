# Generated by Django 4.1.7 on 2023-03-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(height_field='480', null=True, upload_to='cars/', width_field='720'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.ImageField(height_field='480', null=True, upload_to='cars/', width_field='720'),
        ),
    ]
