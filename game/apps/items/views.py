from rest_framework import viewsets
from .serializers import ItemAcquiredSerializer, ItemSerializer
from .models import Item, ItemAcquired
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated


class ItemAcquiredViewSet(viewsets.ModelViewSet):
    serializer_class = ItemAcquiredSerializer
    queryset = ItemAcquired.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ItemAcquired.objects.filter(character__user=user)

