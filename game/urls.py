from django.conf.urls import patterns, include, url
from .views import Homepage
from game.apps.characters.views import CharacterLeaderboard
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^match/', include('game.apps.match.urls',  namespace="match")),
    url(r'^character/', include('game.apps.characters.urls', namespace="character")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^leaderboard/$', CharacterLeaderboard.as_view(), name="leaderbaord"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
