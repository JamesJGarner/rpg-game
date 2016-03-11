from django.conf.urls import include, url
from .views import Homepage
from game.apps.characters.views import CharacterLeaderboard
from django.contrib import admin
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [
    url(r'^match/', include('game.apps.match.urls',  namespace="match")),
    url(r'^character/', include('game.apps.characters.urls', namespace="character")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^leaderboard/$', CharacterLeaderboard.as_view(), name="leaderbaord"),
]
