from django.urls import path
from . import views
from .views import Services_page, Service

urlpatterns = [
    # path("", views.home, name="home"),
    # path("services/", Services_page.as_view(), name='services'),
    # path("service/<int:pk>/", Service.as_view(), name='service'),

    path("", views.coming_soon, name="home"),
]