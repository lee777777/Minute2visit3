# Generated by Django 4.2.4 on 2023-08-21 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_page', '0004_remove_tour_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='description',
            field=models.TextField(default='...'),
        ),
    ]
