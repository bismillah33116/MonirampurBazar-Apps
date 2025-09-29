from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Vendor

# Public: সব ভেন্ডরের লিস্ট দেখাবে
class VendorListView(ListView):
    model = Vendor
    template_name = "vendors/vendor_list.html"
    context_object_name = "vendors"
    paginate_by = 12  # এক পেজে 12টি vendor দেখাবে

# Public: একটি ভেন্ডরের ডিটেইল দেখাবে
class VendorDetailView(DetailView):
    model = Vendor
    template_name = "vendors/vendor_detail.html"
    context_object_name = "vendor"

# Vendor-only dashboard
class VendorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        return self.request.user.is_authenticated and self.request.user.is_vendor

class VendorDashboardView(LoginRequiredMixin, VendorRequiredMixin, TemplateView):
    template_name = "vendors/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendor = self.request.user.vendor
        context["products"] = vendor.product_set.all()
        # Vendor-এর অর্ডার তালিকা এখানে যোগ করতে পারেন
        context["orders"] = []  
        return context

