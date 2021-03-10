from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from visual.models import Hr
from visual.serializers.hr_serializers import HrSerializer


class HrListView(APIView):
    def get(self, request):
        """ return a list of hr data """
        serializer =  HrSerializer(Hr.objects.all(), many=True)
        return Response(serializer.data) 

    def post(self, request):
        """ add a new hr data """
        serializer = HrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HrDetailView(APIView):

    def get_object(self, pk):
        try:
            return Hr.objects.get(pk=pk)
        except Hr.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """ returns a specific hr object """
        hr = self.get_object(pk)
        serializer = HrSerializer(hr)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """ update hr data of given pk """
        hr = self.get_object(pk)
        serializer = HrSerializer(hr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hr = self.get_object(pk)
        hr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)