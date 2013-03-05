from django.conf.urls import patterns, include, url
from django.contrib import admin
from search.views import Buscador
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^cartelera/$', Buscador.as_view()),
	#url(r'^cartelera/$', display_meta),

	#url(r'^resultados/$', Buscador.resultados()),
)