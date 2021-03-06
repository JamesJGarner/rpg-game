from django.conf.urls import patterns, url
from .views import CreateMatch, MatchDetail, AttackForm, MatchList

urlpatterns = [
    url(r'^(?P<pk>\d+)/attack/$', AttackForm.as_view(), name='attack'),
    url(r'^$', MatchList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', MatchDetail.as_view(), name='detail'),
]
