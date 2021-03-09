from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from visual.models import Marketing
from visual.serializers.marketing_serializers import MarketingSerializer

import json

client = Client()

class MarketingTestCases(TestCase):
    def setUp(self):
        self.marketing1 = Marketing.objects.create(month='Jan', 
            social_media_follower=100, website_visitors=500, lead_ratio=5.5)
        self.marketing2 = Marketing.objects.create(month='Feb', 
            social_media_follower=200, website_visitors=1000, lead_ratio=3)
        self.valid_payload = {
            'month': 'Jan',
            'social_media_follower': 400,
            'website_visitors': 1000,
            'lead_ratio': 3.5
        }
        self.invalid_payload = {
            'month': 'False',
            'social_media_follower': 5.5,
            'website_visitors': 1000,
            'lead_ratio': 3.5
        }
        

    def test_marketing_model(self):
        marketing1 = Marketing.objects.get(month='Jan')
        self.assertEqual(marketing1.social_media_follower, 100)
        self.assertEqual(marketing1.website_visitors, 500)
        self.assertEqual(marketing1.lead_ratio, 5.5)

    def test_marketing_list_return(self):
        response = client.get(reverse('marketing_list_view'))
        marketing = Marketing.objects.all()
        serializer = MarketingSerializer(marketing, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_single_customer_return(self):
        response = client.get(
            reverse('marketing_detail_view', kwargs={'pk': self.marketing1.pk}))
        marketing = Marketing.objects.get(pk=self.marketing1.pk)
        serializer = MarketingSerializer(marketing)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_single_marketing_return(self):
        response = client.get(
            reverse('marketing_detail_view', kwargs={'pk': 20}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_marketing(self):
        response = client.post(
            reverse('marketing_list_view'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_marketing(self):
        response = client.post(
            reverse('marketing_list_view'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_marketing_update(self):
        response = client.put(
            reverse('marketing_detail_view', kwargs={'pk': self.marketing1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_marketing_update(self):
        response = client.put(
            reverse('marketing_detail_view', kwargs={'pk': self.marketing1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_marketing(self):
        response = client.delete(
            reverse('marketing_detail_view', kwargs={'pk':self.marketing1.pk}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



        