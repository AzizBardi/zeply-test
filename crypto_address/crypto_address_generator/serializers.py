from rest_framework import serializers

from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'currency', 'address')
        read_only_fields = ('address',)
