from django.views.generic import View
from django.shortcuts import redirect, render
from .models import Order


class CheckoutView(View):
    def get(self, request):
    # show checkout summary
    return render(request, 'orders/checkout.html')


    def post(self, request):
    # create order, mark paid = False (or integrate payment gateway)
    order = Order.objects.create(user=request.user, total_amount=0)
    # add items from cart
    return redirect('orders:order_detail', pk=order.pk)