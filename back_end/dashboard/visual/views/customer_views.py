from django.http import Http404
from django.db.models import Avg, Count, Min, Sum


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from visual.models import Customers
from visual.serializers.customer_serializers import CustomerSerializer


class CustomerListView(APIView):
    def get(self, request):
        """ return a list of customer data """
        serializer =  CustomerSerializer(Customers.objects.all(), many=True)
        return Response(serializer.data) 

    def post(self, request):
        """ add a new marketing data """
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):

    def get_object(self, pk):
        try:
            return Customers.objects.get(pk=pk)
        except Customers.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """ returns a specific customer """
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerAggregateView(APIView):

    def get(self, request):
        """ returns aggregated data of total new customer  """
        response = {}
        total_new_customer = Customers.objects.all().aggregate(Sum('net_new_customer'))
        response['total_new_customer'] = total_new_customer['net_new_customer__sum']
        total_customer = Customers.objects.all().aggregate(Sum('num_of_customer'))
        response['total_customer'] = total_customer['num_of_customer__sum']
        return Response(response)