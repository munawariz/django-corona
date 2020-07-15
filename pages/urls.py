from django.urls import path, include, re_path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index),
    path('countries/', views.list_country),
    re_path(r'^countries/(?P<country_requested>[\w|\W]+)/$', views.country),
]