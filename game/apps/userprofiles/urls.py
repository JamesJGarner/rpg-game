from django.conf.urls import patterns, url
from .views import UserProfilePage, chart

urlpatterns = [
    url(r'^user/(?P<pk>\d+)/$', UserProfilePage.as_view(), name="profile_page"),
    url(r'^character/$', chart, name="profile_page"),
    
]
