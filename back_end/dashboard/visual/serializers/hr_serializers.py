from rest_framework import serializers

from visual.models import Hr


class HrSerializer(serializers.ModelSerializer):
    """ serializes hr data """

    class Meta:
        model = Hr
        fields = '__all__'