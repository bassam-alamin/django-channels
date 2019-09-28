# dj_channels/urls.py
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^chat/', include('example.urls')),
    url(r'^admin/', admin.site.urls),
]

