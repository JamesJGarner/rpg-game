from django.conf.urls import patterns, url
from .views import UserProfilePage, CharacterImage

urlpatterns = [
    url(r'^user/(?P<pk>\d+)/$', UserProfilePage.as_view(), name="profile_page"),
    url(r'^image/(?P<pk>\d+)/$', CharacterImage, name="CharacterImage"),
]
