from .models import Item, Position, ItemAcquired
from rest_framework import serializers
from django.core.exceptions import ValidationError


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name', 'position', 'image')


class ItemAcquiredSerializer(serializers.ModelSerializer):

    item = ItemSerializer(
        read_only=True,
    )

    def validate(self, attrs):
        for attr in attrs:
            setattr(self.instance, attr, attrs[attr])

        self.instance.clean()
        return attrs

    class Meta:
        model = ItemAcquired
        fields = ('id', 'character', 'item', 'equipped_to')
