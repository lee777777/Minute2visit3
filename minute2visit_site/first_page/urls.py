from django.urls import path
from . import views
from .views import Services_page

urlpatterns = [
    # path("", views.home, name="home"),
    # path("services/", Services_page.as_view(), name='services'),
    # path("service/<int:pk>/", views.service, name='service'),
    # path("contact_us/", views.contact, name='contact_us'),
     path("", views.coming_soon, name="home"),
]