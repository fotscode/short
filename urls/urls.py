from django.urls import path

from . import views

app_name='urls'
urlpatterns = [
     path('', views.index, name='index'),
     path('<str:short>/', views.redirect, name='redirect'),
#    path('<str:url_short>/detail/', views.DetailView.as_view(), name='detail'),
]
