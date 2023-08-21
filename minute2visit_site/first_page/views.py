from django.shortcuts import render
from .models import Tour
from django.views.generic import ListView, DetailView
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
    
class Service(DetailView):
    model = Tour
    template_name = 'service.html'  # <app>/<model>_<viewtype>.html


def coming_soon(request):    
    context = {
        'active_page': 'coming_soon'
    }
    return render(request, 'coming_soon.html', context)