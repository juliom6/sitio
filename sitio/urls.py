from django.conf.urls import patterns, include, url
from django.contrib import admin
from search.views import Buscador
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', Buscador.as_view()),
)