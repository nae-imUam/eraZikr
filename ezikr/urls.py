from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path("<int:task_id>/", views.Next, name="next"),
    path("certify/", views.Certify, name="certify"),
]
