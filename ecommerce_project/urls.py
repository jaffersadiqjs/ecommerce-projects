from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to E-Commerce Platform</h1><p><a href='/orders/place/'>Place an Order</a> | <a href='/orders/contact/'>Contact Us</a></p>")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("orders/", include("orders.urls")),
    path("accounts/", include("django.contrib.auth.urls")),  # 👈 Add this
]
