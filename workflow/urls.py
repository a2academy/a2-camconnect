from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("features/", views.features, name="features"),
    path("brands/", views.brands, name="brands"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("reset/", views.reset, name="reset"),
]
