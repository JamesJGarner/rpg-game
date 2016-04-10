from django.conf.urls import patterns, url
from .views import MessageList

urlpatterns = [
    url(r'^$', MessageList.as_view(), name="MessageList"),
]
