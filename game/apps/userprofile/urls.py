from django.conf.urls import patterns, url
from .views import UserProfilePage

urlpatterns = [
    url(r'^settings/$', UserProfilePage.as_view(), name="profile_page"),
]
