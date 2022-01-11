from django.urls import path

from . import views

app_name = "urls"
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("<str:short>/", views.redirect, name="redirect"),
    path('<str:short>/detail/', views.detail, name='detail'),
]
