from django.urls import path

from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    # path("services/", views.services_page, name="services"),
    #  path("service/", views.service, name="service"),
      path("", views.coming_soon, name="home"),
]