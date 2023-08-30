from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Day
from django.core.mail import send_mail
from .models import Booking
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@receiver([post_save, post_delete], sender=Day)
def update_day_number_orders(sender, instance, **kwargs):
    tour = instance.tour
    days = tour.days.all().order_by('number_order')

    for idx, day in enumerate(days, start=1):
        day.number_order = idx
        day.save()
        
# @receiver(post_save, sender=Booking)
# def send_booking_emails(sender, instance, created, **kwargs):
#     if created:
#         # Send email to user who booked
#         subject_user = 'Tour Booking Confirmation'
#         message_user = 'Thank you for booking! You will receive an email confirmation soon.'
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list_user = [instance.email]
#         try:
#          send_mail(subject_user, message_user, from_email, recipient_list_user, fail_silently=True)
#         except Exception as e:
#          logger.error(f"Error sending user confirmation email: {e}")

      
#         subject = 'New Tour Booking'
#         message = f'A new tour booking was made by {instance.first_name} {instance.last_name}'
#         recipient = settings.RECIPIENT_ADDRESS
#         send_mail(subject, message, from_email, recipient, fail_silently=True)