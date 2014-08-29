from django.conf.urls import patterns, url
from .views import UserProfilePage

urlpatterns = patterns('',
    url(r'^settings/$', UserProfilePage.as_view(), name="profile_page"),
)
