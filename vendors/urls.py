from django.urls import path
from .import views

app_name = "vendors"

urlpatterns = [
    path("", views.VendorListView.as_view(), name="vendor_list"),
    path("<slug:slug>/", views.VendorDetailView.as_view(), name="vendor_detail"),
    path("dashboard/", views.VendorDashboardView.as_view(), name="dashboard"),
]
