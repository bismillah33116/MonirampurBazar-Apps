# products/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product

# Optional: Vendor-only access mixin
class VendorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        # ধরে নিচ্ছি আপনার User মডেলে is_vendor ফিল্ড আছে
        return self.request.user.is_authenticated and getattr(self.request.user, 'is_vendor', False)

class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
   

# Product list view
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(available=True)

# Product detail view
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
