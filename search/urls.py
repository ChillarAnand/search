from django.conf.urls import url
from django.contrib import admin

from document.views import index, search


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^index', index, name='index'),

    url(r'^search', search, name='search'),
]
