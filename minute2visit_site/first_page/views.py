from django.shortcuts import render
from .models import Tour, CancellationPolicy, TermsAndConditions, Included, Excluded
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
    template_name = 'service.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add data from other models to the context
        context['cancellation_policy'] = CancellationPolicy.objects.all()
        context['terms_and_conditions'] = TermsAndConditions.objects.all()
        context['included'] = Included.objects.all()
        context['excluded'] = Excluded.objects.all()
        
        return context


def coming_soon(request):    
    context = {
        'active_page': 'coming_soon'
    }
    return render(request, 'coming_soon.html', context)