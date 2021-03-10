from rest_framework import serializers

from visual.models import Customers


class CustomerSerializer(serializers.ModelSerializer):
    """ serializes customer data """

    class Meta:
        model = Customers 
        fields = '__all__'