from django import forms
from .models import Booking
from django.core.mail import send_mail
from django.conf import settings
import logging

class BookingForm(forms.ModelForm):
    
    
    class Meta:
        model = Booking
        fields = [ 'first_name', 'last_name', 'phone_number', 'email', 'num_pax']
        
    def get_info(self):
    
        # Cleaned data
         cl_data = super().clean()

         first_name = cl_data.get('first_name').strip()
         last_name = cl_data.get('last_name').strip()
         client_email = cl_data.get('email')
         phone_number = cl_data.get('phone_number')
         num_pax =cl_data.get('num_pax')
         client_subject = "Tour Booking Confirmation"
         our_subject = "New Tour Booking"
         client_msg = 'Thank you for booking! You will receive an email confirmation soon.'
         client_msg += f'\n"This is your information:"\n'
         client_msg += f'name: {first_name} {last_name}, phone number: {phone_number}, number of pax: {num_pax}'
         our_msg = 'New Tour Booking!'
         our_msg += f'\n"This is the client information:"\n'
         our_msg += f'name: {first_name} {last_name}, phone number: {phone_number}, number of pax: {num_pax}'

         return client_email,client_subject,our_subject, client_msg,our_msg

    def send(self):

         client_email,client_subject,our_subject, client_msg,our_msg = self.get_info()
         logger = logging.getLogger(__name__)
         logger.debug("Some variable: %s", client_email)
         print("ddddddddddddddddddddd",client_email,client_subject,our_subject, client_msg,our_msg )
         send_mail(
            subject=our_subject,
            message=our_msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
         send_mail(
            subject=client_subject,
            message=client_msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client_email],
            fail_silently=False,
        )

         
        
        