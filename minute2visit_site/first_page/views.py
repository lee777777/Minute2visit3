from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'active_page': 'home'
    }
    return render(request, 'home.html', context)
def services_page(request):    
    context = {
        'active_page': 'services'
    }
    return render(request, 'services.html', context)

def service(request):    

    return render(request, 'service.html')
def coming_soon(request):    
    context = {
        'active_page': 'coming_soon'
    }
    return render(request, 'coming_soon.html', context)