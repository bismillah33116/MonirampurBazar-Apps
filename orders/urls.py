from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    # Customer side
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("my-orders/", views.CustomerOrderListView.as_view(), name="my_orders"),
    path("my-orders/<int:pk>/", views.CustomerOrderDetailView.as_view(), name="my_order_detail"),

    # Vendor side
    path("vendor-orders/", views.VendorOrderListView.as_view(), name="vendor_orders"),
    path("vendor-orders/<int:pk>/", views.VendorOrderDetailView.as_view(), name="vendor_order_detail"),

    # Admin / Staff side
    path("all/", views.AdminOrderListView.as_view(), name="all_orders"),
    path("all/<int:pk>/", views.AdminOrderDetailView.as_view(), name="order_detail"),
]
