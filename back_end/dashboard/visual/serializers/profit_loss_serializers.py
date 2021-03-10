from rest_framework import serializers

from visual.models import ProfitLoss


class ProfitLossSerializer(serializers.ModelSerializer):
    """ serializes profit loss data """

    class Meta:
        model = ProfitLoss
        fields = '__all__'