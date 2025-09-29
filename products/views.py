# products/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product

# Optional: Vendor-only access mixin
class VendorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        # ধরে নিচ্ছি আপনার User মডেলে is_vendor ফিল্ড আছে
        return self.request.user.is_authenticated and getattr(self.request.user, 'is_vendor', False)

# Home page view using TemplateView
class HomeTemplateView(TemplateView):
    template_name = 'products/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # সর্বশেষ 6টি available product
        context['products'] = Product.objects.filter(available=True)[:6]
        context['site_name'] = 'মণিরামপুর বাজার'
        return context

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
