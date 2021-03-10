from django.http import Http404
from django.db.models import Avg, Count, Min, Sum


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from visual.models import ProductDevelopment
from visual.serializers.product_development_serializer import ProductDevelopmentSerializer


class ProductDevelopmentListView(APIView):

    def get(self, request):
        """ return a list of prod dev data """
        serializer =  ProductDevelopmentSerializer(ProductDevelopment.objects.all(), many=True)
        return Response(serializer.data) 

    def post(self, request):
        """ add a new prod dev data """
        serializer = ProductDevelopmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDevelopmentDetailView(APIView):

    def get_object(self, pk):
        try:
            return ProductDevelopment.objects.get(pk=pk)
        except ProductDevelopment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """ returns a specific product development object """
        product_dev = self.get_object(pk)
        serializer = ProductDevelopmentSerializer(product_dev)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """ update a specific product development object """
        product_dev = self.get_object(pk)
        serializer = ProductDevelopmentSerializer(product_dev, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product_dev = self.get_object(pk)
        product_dev.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductDevelopmentAggregateView(APIView):

    def get(self, request):
        """ returns avg test accuracy, avg test coverage  """
        response = {}
        avg_test_accuracy = ProductDevelopment.objects.all().aggregate(Avg('test_accuracy'))
        response['avg_test_accuracy'] = round(avg_test_accuracy['test_accuracy__avg'], 2)
        avg_test_coverage = ProductDevelopment.objects.all().aggregate(Avg('test_coverage'))
        response['avg_test_coverage'] = round(avg_test_coverage['test_coverage__avg'], 2)

        return Response(response)