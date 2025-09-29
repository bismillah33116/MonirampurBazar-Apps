from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserRegisterForm



class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_orders"] = self.request.user.order_set.all() if hasattr(self.request.user, "order_set") else []
        context["vendor"] = getattr(self.request.user, "vendor", None)
        return context

# User Registration View
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        role = form.cleaned_data.get("role")
        Profile.objects.create(user=self.object, role=role, is_vendor=(role=="vendor"))
        return response