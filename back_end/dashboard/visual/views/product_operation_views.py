from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from visual.models import ProductOperation
from visual.serializers.product_operation_serializer import ProductOperationSerializer


class ProductOperationListView(APIView):
    def get(self, request):
        """ return a list of customer data """
        serializer =  ProductOperationSerializer(ProductOperation.objects.all(), many=True)
        return Response(serializer.data) 

    def post(self, request):
        """ add a new marketing data """
        serializer = ProductOperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductOperationDetailView(APIView):

    def get_object(self, pk):
        try:
            return ProductOperation.objects.get(pk=pk)
        except ProductOperation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """ returns a specific product operation objrct """
        product_operation = self.get_object(pk)
        serializer = ProductOperationSerializer(product_operation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product_operation = self.get_object(pk)
        serializer = ProductOperationSerializer(product_operation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product_operation = self.get_object(pk)
        product_operation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)