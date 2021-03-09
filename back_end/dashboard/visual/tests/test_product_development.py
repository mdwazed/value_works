from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from visual.models import ProductDevelopment
from visual.serializers.product_development_serializer import ProductDevelopmentSerializer

import json

client = Client()

class ProductDevelopmentTestCases(TestCase):
    def setUp(self):
        self.pd1 = ProductDevelopment.objects.create(month='Jan', 
            dev_freq=100, test_accuracy=50, test_coverage=60)
        self.pd2 = ProductDevelopment.objects.create(month='Feb', 
            dev_freq=50, test_accuracy=55, test_coverage=65)
        self.valid_payload = {
            'month': 'Jan',
            'dev_freq': 80,
            'test_accuracy': 80.5,
            'test_coverage': 30.5
        }
        self.invalid_payload = {
            'month': 'False',
            'dev_freq': 80,
            'test_accuracy': 80.5,
            'test_coverage': 30.5
        }
        

    def test_product_development_model(self):
        pd1 = ProductDevelopment.objects.get(month='Jan')
        self.assertEqual(pd1.dev_freq, 100)
        self.assertEqual(pd1.test_accuracy, 50)
        self.assertEqual(pd1.test_coverage, 60)

    def test_product_development_list_return(self):
        response = client.get(reverse('product_development_list_view'))
        pd = ProductDevelopment.objects.all()
        serializer = ProductDevelopmentSerializer(pd, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_single_product_development_return(self):
        response = client.get(
            reverse('product_development_detail_view', kwargs={'pk': self.pd1.pk}))
        pd = ProductDevelopment.objects.get(pk=self.pd1.pk)
        serializer = ProductDevelopmentSerializer(pd)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_single_pd_return(self):
        response = client.get(
            reverse('product_development_detail_view', kwargs={'pk': 20}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_pd(self):
        response = client.post(
            reverse('product_development_list_view'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_pd(self):
        response = client.post(
            reverse('product_development_list_view'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_pd_update(self):
        response = client.put(
            reverse('product_development_detail_view', kwargs={'pk': self.pd1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_pd_update(self):
        response = client.put(
            reverse('product_development_detail_view', kwargs={'pk': self.pd1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_pd(self):
        response = client.delete(
            reverse('product_development_detail_view', kwargs={'pk':self.pd1.pk}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



        