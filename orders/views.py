# orders/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import OrderForm, ContactForm
from .models import Order

@login_required
def place_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            # Send confirmation email
            subject = "Order Confirmation"
            message = (
                f"Hello {request.user.username},\n\n"
                f"Your order has been placed successfully.\n"
                f"Order ID: {order.order_id}\n"
                f"Total Amount: ${order.total_amount}\n\n"
                f"Thank you for shopping with us!"
            )
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [request.user.email])

            return render(request, "orders/order_success.html", {"order": order})
    else:
        form = OrderForm()
    return render(request, "orders/order_form.html", {"form": form})

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                f"Customer Query from {name}",
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
            )
            return render(request, "orders/contact_success.html")
    else:
        form = ContactForm()
    return render(request, "orders/contact_form.html", {"form": form})
