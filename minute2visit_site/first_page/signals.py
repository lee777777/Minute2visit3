from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Day

@receiver([post_save, post_delete], sender=Day)
def update_day_number_orders(sender, instance, **kwargs):
    tour = instance.tour
    days = tour.days.all().order_by('number_order')

    for idx, day in enumerate(days, start=1):
        day.number_order = idx
        day.save()