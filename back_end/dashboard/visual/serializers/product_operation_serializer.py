from rest_framework import serializers

from visual.models import ProductOperation


class ProductOperationSerializer(serializers.ModelSerializer):
    """ serializes producrt operation data """

    class Meta:
        model = ProductOperation
        fields = '__all__'