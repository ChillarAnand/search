from django.conf.urls import url

from document.views import index, search, home


urlpatterns = [
    url(r'^$', home, name='home'),

    url(r'^index', index, name='index'),

    url(r'^search', search, name='search'),
]
