from django.urls import path, include, re_path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index),
    path('global/', views.global_case),
    path('list_country/', views.list_country),
    re_path(r'^(?P<country_requested>[\w-]+)/$', views.country),
]