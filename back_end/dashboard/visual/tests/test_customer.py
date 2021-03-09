from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from visual.models import Customers
from visual.serializers.customer_serializers import CustomerSerializer

import json

client = Client()

class CustomerTestCases(TestCase):
    def setUp(self):
        self.customer1 = Customers.objects.create(month='Jan', net_promoter_score=3, 
            net_new_customer=22, num_of_customer=200)
        self.customer2 = Customers.objects.create(month='Feb', net_promoter_score=4, 
            net_new_customer=42, num_of_customer=400)
        self.valid_payload = {
            'month': 'Jan',
            'net_promoter_score': 4,
            'net_new_customer': 50,
            'num_of_customer': 200
        }
        self.invalid_payload = {
            'month': 'False',
            'net_promoter_score': 4,
            'net_new_customer': 50,
            'num_of_customer': 200
        }
        

    def test_customer_model(self):
        customer1 = Customers.objects.get(month='Jan')
        customer2 = Customers.objects.get(month='Feb')
        self.assertEqual(customer1.net_promoter_score, 3)
        self.assertEqual(customer1.net_new_customer, 22)
        self.assertEqual(customer1.num_of_customer, 200)

    def test_customer_list_return(self):
        response = client.get(reverse('customer_list_view'))
        customers = Customers.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_single_customer_return(self):
        response = client.get(
            reverse('customer_detail_view', kwargs={'pk': self.customer1.pk}))
        customer = Customers.objects.get(pk=self.customer1.pk)
        serializer = CustomerSerializer(customer)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_single_customer_return(self):
        response = client.get(
            reverse('customer_detail_view', kwargs={'pk': 20}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_customer(self):
        response = client.post(
            reverse('customer_list_view'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_customer(self):
        response = client.post(
            reverse('customer_list_view'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_customer_update(self):
        response = client.put(
            reverse('customer_detail_view', kwargs={'pk': self.customer1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_customer_update(self):
        response = client.put(
            reverse('customer_detail_view', kwargs={'pk': self.customer1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_customer(self):
        response = client.delete(
            reverse('customer_detail_view', kwargs={'pk':self.customer1.pk}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



        