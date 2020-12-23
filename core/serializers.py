from rest_framework import serializers

from core.models import FIO, Type, Phones, Addresses


class FIOSerializer(serializers.ModelSerializer):
    class Meta:
        model = FIO
        fields = '__all__'


class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'
