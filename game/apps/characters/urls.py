from django.conf.urls import patterns, url
from .views import CharacterDetail, CharacterCreate, ShopItems

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)$', CharacterDetail.as_view(), name='detail'),
    url(r'^create/$', CharacterCreate.as_view(), name='create'),
    url(r'^shop/$', ShopItems.as_view(), name='shop'),
)
