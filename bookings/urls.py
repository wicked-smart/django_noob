from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("flight/<int:flight_id>", views.flight, name="flight"),
    path("flight/<int:flight_id>/book", views.book, name="book")
]