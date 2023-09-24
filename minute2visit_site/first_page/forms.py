from django import forms
from .models import Booking
from django.core.mail import send_mail
from django.conf import settings
from django_countries.fields import CountryField

class BookingForm(forms.ModelForm):
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(attrs={ 'class':'form-control',  'aria-label':'First name'})
    )
    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(attrs={'class':'form-control','aria-label':'Last name'})
    )
    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={ 'class':'form-control'})
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class':'form-control', 'id':'inputEmail4'})
    )
    num_pax = forms.ChoiceField(
        label="Number of Pax",
        choices=[
            ("2-4", "Two to four"),
            ("5-9", "Five to nine"),
            ("10-15", "Ten to fifteen"),
            ("16-20", "Sixteen to twenty"),
        ],
        widget=forms.Select(attrs={'class':'form-select text-center'})
    )
    notes = forms.CharField(
        label="Notes",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder':'leave us a note if you feel like it...'}),
        required=False
    )
    
    
    class Meta:
        model = Booking
        fields = [ 'first_name', 'last_name', 'phone_number', 'email', 'num_pax', 'notes']

        # def __init__(self, *args, **kwargs):
        #   super(BookingForm, self).__init__(*args, **kwargs)
        #   self.fields['first_name'].widget.attrs.update({'class': 'form-control','aria-label':'First name'})
        #   self.fields['last_name'].widget.attrs.update({'class': 'form-control','aria-label':'Last name'})
        #   self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        #   self.fields['email'].widget.attrs.update({'class': 'form-control', 'id':'inputEmail4'})
        #   self.fields['num_pax'].widget.attrs.update({'class': 'form-select'})
        
    def get_info(self):
    
        # Cleaned data
         cl_data = super().clean()
         notes = cl_data.get('notes')
         first_name = cl_data.get('first_name').strip()
         last_name = cl_data.get('last_name').strip()
         client_email = cl_data.get('email')
         phone_number = cl_data.get('phone_number')
         num_pax =cl_data.get('num_pax')
         client_subject = "Tour Booking Confirmation"
         our_subject = "New Tour Booking"
         client_msg = 'Thank you for booking! You will receive an email confirmation soon.'
         client_msg += f'\nThis is your information:\n'
         client_msg += f'name: {first_name} {last_name}, phone number: {phone_number}, number of pax: {num_pax}'
         our_msg = 'New Tour Booking!'
         our_msg += f'\nThis is the client information:\n'
         our_msg += f'name: {first_name} {last_name}, phone number: {phone_number}, number of pax: {num_pax}'
         if notes:
          client_msg += f'\nAdditional notes: {notes}'
          our_msg += f'\nAdditional notes from the client: {notes}'
         return client_email,client_subject,our_subject, client_msg,our_msg

    def send(self):

         client_email,client_subject,our_subject, client_msg,our_msg = self.get_info()
       
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

class ContactForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'John'})
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Smith'})
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class':'form-control', 'id':'inputEmail4', 'placeholder':'example@gmail.com'})
    )
    subject = forms.CharField(
        max_length=100,
        label="Subject",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject of message'})
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'class':'form-control', 'id':'exampleFormControlTextarea1', 'rows':'5', 'placeholder':'Your feedback or inquiry massege here'})
    )
    cc_myself = forms.BooleanField(
        label="CC Myself",
        
        widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),required=False)
   
    def get_info(self):
    
        # Cleaned data
         cl_data = super().clean()
         
         first_name = cl_data.get('first_name').strip()
         last_name = cl_data.get('last_name').strip()
         name = f"{first_name} {last_name}"

         client_email = cl_data.get('email')
         subject = cl_data.get('subject')
         client_subject = f"{subject} - CONTACT US"
         msg = cl_data.get('message')
         client_msg = f"from {name}:\n\n {msg}"
         return client_email,client_subject,client_msg

    def send(self, cc):
        client_email,client_subject,client_msg =  self.get_info()
        
        if cc:
           send_mail(
            subject=client_subject,
            message=client_msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS, client_email],
            fail_silently=False,
        ) 
        else:
            send_mail(
            subject=client_subject,
            message=client_msg,
            from_email=client_email,
            recipient_list=[settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        ) 
class WeatherForm(forms.Form):
        city = forms.ChoiceField(
        label="City",
        choices=[
            ("23.5841300,58.4077800", "Muscat"),
            ("22.5666700,59.5288900", "Sur"),
            ("22.9333300,57.5333300", "Nizwa"),
        ],
        widget=forms.Select(attrs={'class':'form-select text-center'})
    )
        
        