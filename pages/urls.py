from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.index),
    path('dev/', views.dev),
    path('countries/', views.list_country),
    re_path(r'^countries/(?P<country_requested>[\w|\W]+)/$', views.country),
]

handler404 = 'pages.views.error_404'