from django.conf.urls import include, url
from .views import Homepage
from game.apps.characters.views import CharacterLeaderboard
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()
from rest_framework import routers
from game.apps.items import views

router = routers.DefaultRouter()
router.register(r'item', views.ItemViewSet)
router.register(r'items', views.ItemAcquiredViewSet)



urlpatterns = [
	url(r'^api/', include(router.urls)),
    url(r'^match/', include('game.apps.matches.urls',  namespace="match")),
    url(r'^character/', include('game.apps.characters.urls', namespace="character")),
    url(r'^', include('game.apps.userprofiles.urls', namespace="userprofile")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^leaderboard/$', CharacterLeaderboard.as_view(), name="leaderbaord"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
