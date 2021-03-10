from rest_framework import serializers

from visual.models import ProductDevelopment


class ProductDevelopmentSerializer(serializers.ModelSerializer):
    """ serializes producrt development data """

    class Meta:
        model = ProductDevelopment
        fields = '__all__'