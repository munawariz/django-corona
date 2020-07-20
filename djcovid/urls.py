from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', include('pages.urls')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'pages.views.error_404'
handler500 = 'pages.views.error_500'