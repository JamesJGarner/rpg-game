from django.conf.urls import patterns, url
from .views import CharacterDetail, CharacterCreate, CreateMatch, CharacterImage

urlpatterns = [
    url(r'^(?P<pk>\d+)$', CharacterDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/create/$', CreateMatch.as_view(), name='create'),
    url(r'^create/$', CharacterCreate.as_view(), name='create_char'),
    url(r'^(?P<pk>\d+)/image/$', CharacterImage, name="CharacterImage"),
]
