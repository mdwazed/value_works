from django.http import Http404
from django.db.models import Avg, Count, Min, Sum

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from visual.models import Marketing
from visual.serializers.marketing_serializers import MarketingSerializer

import json


class MarketingListView(APIView):
    
    def get(self, request):
        """ return a list of marketing data """
        serializer =  MarketingSerializer(Marketing.objects.all(), many=True)
        return Response(serializer.data) 

    def post(self, request):
        """ add a new marketing data """
        serializer = MarketingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarketingDetailView(APIView):

    def get_object(self, pk):
        try:
            return Marketing.objects.get(pk=pk)
        except Marketing.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """ returns a specific customer """
        marketing = self.get_object(pk)
        serializer = MarketingSerializer(marketing)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        marketing = self.get_object(pk)
        serializer = MarketingSerializer(marketing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        marketing = self.get_object(pk)
        marketing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MarketingAggregateView(APIView):

    def get(self, request):
        """ returns aggregated data of social media follower and website visitors  """
        response = {}
        total_followers = Marketing.objects.all().aggregate(Sum('social_media_follower'))
        response['total_followers'] = total_followers['social_media_follower__sum']
        total_visitors = Marketing.objects.all().aggregate(Sum('website_visitors'))
        response['total_visitors'] = total_visitors['website_visitors__sum']
        return Response(response)
