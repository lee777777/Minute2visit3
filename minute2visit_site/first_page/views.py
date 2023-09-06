from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import BookingForm, ContactForm, WeatherForm
from .models import Tour, CancellationPolicy, TermsAndConditions, Included, Excluded
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.conf import settings
from django.urls import reverse_lazy
import requests
from django.http import JsonResponse
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
def home(request):

    default_city = "23.5841300,58.4077800"  # Default to Muscat
    city = default_city 
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
       weather_form = WeatherForm(request.POST)
       if weather_form.is_valid():
         city = weather_form.cleaned_data["city"]
         lat, lon = city.split(',')
         url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.OPENWEATHER_API_KEY}'
         city_weather = requests.get(url).json()
         temp = round(float(city_weather['main']['temp']) - 273.15, 2)
         weather_data = {
                'temperature': temp,
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }

         return JsonResponse(weather_data, status=200)
       else:
            errors = weather_form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)
    else:
     weather_form = WeatherForm()
     url = f'https://api.openweathermap.org/data/2.5/weather?lat=23.5841300&lon=58.4077800&appid={settings.OPENWEATHER_API_KEY}'
     city_weather = requests.get(url).json()
     temp = round(float(city_weather['main']['temp']) - 273.15, 2)

     
    context = {
        'active_page': 'home',
        'weather_form':weather_form,
        'city' : city,
        'temperature' : temp,
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    return render(request, 'home.html', context)
class Services_page(ListView):
    model = Tour
    template_name = 'services.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'tours'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'services'
        return context

    
    # def post(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     booking_form = context['booking_form']

    #     if booking_form.is_valid():
    #         booking = booking_form.save(commit=False)
    #         booking.tour = self.get_object()  # Link the booking to the current tour
    #         booking.save()
            

    #         return HttpResponseRedirect(self.request.path)

    #     # If form is not valid, re-render the page with errors
    #     return self.render_to_response(context)

def service(request, pk):
    tour = Tour.objects.get(pk=pk)

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.tour = tour
            booking.save()
            booking_form.send()
            first_name =  booking_form.cleaned_data['first_name']
            last_name = booking_form.cleaned_data['last_name']
            # messages.success(request, f'Thank you for booking! You will receive an email confirmation soon.')
            # return redirect('service', pk=pk)
            booking_data = {
                'message': f'Thank you {first_name} {last_name} for booking! You will receive an email confirmation soon.',
            }

            return JsonResponse(booking_data, status=200)
            
        else:
            errors = booking_form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)
    else:
        booking_form = BookingForm()
    
    
    context = {
        'tour':tour,
        'cancellation_policy': CancellationPolicy.objects.all(),
        'terms_and_conditions': TermsAndConditions.objects.all(),
        'included': Included.objects.all(),
        'excluded': Excluded.objects.all(),
        'booking_form':booking_form
    }
    
    return render(request, 'service.html', context)


def contact(request):    
    if request.method == 'POST':
       contact_form = ContactForm(request.POST)
       if contact_form.is_valid():
           cc = contact_form.cleaned_data["cc_myself"]
           contact_form.send(cc)
           messages.success(request, f'Thank you for getting in touch with us! Your message has been successfully sent. We will get back to you shortly.')
           return redirect('contact_us')
    else:
        contact_form = ContactForm()    
    context = {
        'contact_form':contact_form,
        'active_page': 'contact_us'
    }     
    return render(request, 'contact_us.html', context)

def about(request):    
 
    context = {
        'active_page': 'about_us'
    }     
    return render(request, 'about_us.html', context)


def coming_soon(request):    
    context = {
        'active_page': 'coming_soon'
    }
    return render(request, 'coming_soon.html', context)