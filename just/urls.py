# from django.http import HttpResponse
from django.urls import path
from .views import Home, About, Contact
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Home),
    path('about', About),
    path('contact', Contact),
    path('admin/', admin.site.urls)
]+static(
    settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT
)