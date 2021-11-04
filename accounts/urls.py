from django.urls import path
from . import views

app_name = "localaccounts"

urlpatterns = [
    path("dashboard/", views.account_dashboard, name="account_dashboard"),
]
