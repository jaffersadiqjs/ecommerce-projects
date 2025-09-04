# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("place/", views.place_order, name="place_order"),
    path("contact/", views.contact_view, name="contact"),
]
