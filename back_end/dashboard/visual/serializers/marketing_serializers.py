from rest_framework import serializers

from visual.models import Marketing


class MarketingSerializer(serializers.ModelSerializer):
    """ serializes marketing data """

    class Meta:
        model = Marketing 
        fields = '__all__'