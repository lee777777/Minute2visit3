from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Tour, CancellationPolicy, TermsAndConditions, Included, Excluded
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
def home(request):
    context = {
        'active_page': 'home'
    }
    return render(request, 'home.html', context)
class Services_page(ListView):
    model = Tour
    template_name = 'services.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'tours'
    

    
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

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.tour = tour
            booking.save()
            booking_form.send()
            messages.success(request, f'Thank you for booking! You will receive an email confirmation soon.')
            return redirect('service', pk=pk)
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

def coming_soon(request):    
    context = {
        'active_page': 'coming_soon'
    }
    return render(request, 'coming_soon.html', context)