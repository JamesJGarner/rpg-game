from django.conf.urls import patterns, include, url
from .views import Homepage
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^match/', include('game.apps.match.urls',  namespace="match")),
    url(r'^character/', include('game.apps.characters.urls', namespace="character")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Homepage.as_view(), name='homepage'),
)
