from django.http import Http404
from django.db.models import Avg, Count, Min, Sum

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from visual.models import ProfitLoss
from visual.serializers.profit_loss_serializers import ProfitLossSerializer


class ProfitLossListView(APIView):
    def get(self, request):
        """ return a list of profit loss data """
        serializer =  ProfitLossSerializer(ProfitLoss.objects.all(), many=True)
        return Response(serializer.data) 

    def post(self, request):
        """ add a new profit loss data """
        serializer = ProfitLossSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfitLossDetailView(APIView):

    def get_object(self, pk):
        try:
            return ProfitLoss.objects.get(pk=pk)
        except ProfitLoss.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """ returns a specific profitloss object """
        profitloss = self.get_object(pk)
        serializer = ProfitLossSerializer(profitloss)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """ update specific profit loss object """
        profitloss = self.get_object(pk)
        serializer = ProfitLossSerializer(profitloss, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        proiftloss = self.get_object(pk)
        proiftloss.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfitLossAggregateView(APIView):

    def get(self, request):
        """ returns aggregated data of profit loss  """
        response = {}
        avg_software_rev = ProfitLoss.objects.all().aggregate(Avg('software_revenue'))
        response['avg_software_rev'] = round(avg_software_rev['software_revenue__avg'], 2)
        avg_other_rev = ProfitLoss.objects.all().aggregate(Avg('other_revenue'))
        response['avg_other_rev'] = round(avg_other_rev['other_revenue__avg'], 2)
        avg_svc_rev = ProfitLoss.objects.all().aggregate(Avg('professional_service_revenue'))
        response['avg_svc_rev'] = round(avg_svc_rev['professional_service_revenue__avg'], 2)
        return Response(response)