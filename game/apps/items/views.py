from rest_framework import viewsets
from .serializers import ItemAcquiredSerializer, ItemSerializer
from .models import Item, ItemAcquired
from django.http import HttpResponse


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that lets you see all the items.
    """
    #TODO: Add later that it only returns the items they have (more for the point of view that a user can't see all the items in the system)
    queryset = ItemAcquired.objects.all()
    serializer_class = ItemSerializer


class ItemAcquiredViewSet(viewsets.ModelViewSet):
    serializer_class = ItemAcquiredSerializer
    queryset = ItemAcquired.objects.all()

    def get_queryset(self):
        user = self.request.user
        return ItemAcquired.objects.filter(character__user=user)

