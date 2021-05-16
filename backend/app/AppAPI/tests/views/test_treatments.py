from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from AppAPI.models import Treatment
from AppAPI.serializers import TreatmentSerializer
from uuid import UUID
from collections import OrderedDict


class TreatmentTestCase(APITestCase):

    treatment_url = "/api/treatments/"

    def setUp(self):

        self.owner = get_user_model().objects.create(
            email="testemail@test.com",
            password="testpassword"
        )

        tokens = RefreshToken.for_user(self.owner)
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + str(tokens.access_token)
        )
        
        Treatment.objects.create(
            associated_user = self.owner,
            name = "John's treatment",
            beneficiary = "John"
        )

    def test_get_all_treatments(self):
        treatment1 = Treatment.objects.get(name="John's treatment")
    
        temp = OrderedDict(
            uuid = str(treatment1.uuid),
            associated_user = UUID(str(treatment1.associated_user.uuid)),
            name = treatment1.name,
            beneficiary = treatment1.beneficiary
            )
    
        expected_data = [temp]

        response = self.client.get(self.treatment_url, {"beneficiary": treatment1.beneficiary})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
  
    def test_get_single_treatment(self):
       
        treatment1 = Treatment.objects.get(name="John's treatment")

        expected_data = {
            'uuid': str(treatment1.uuid),
            'associated_user': treatment1.associated_user.uuid,
            'name': treatment1.name,
            'beneficiary': treatment1.beneficiary
        }

        response = self.client.get(self.treatment_url + str(treatment1.uuid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_create_treatment(self):
        body = OrderedDict(
            name = "Peter's treatment",
            beneficiary = "Peter"
            )

        response = self.client.post(
            self.treatment_url, 
            body,
            format="json"
            )

        treatment1 = Treatment.objects.get(name="Peter's treatment")

        expected_data = {
            'uuid': str(treatment1.uuid),
            'associated_user': treatment1.associated_user.uuid,
            'name': "Peter's treatment",
            'beneficiary': "Peter"
        }
        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_data)
 
    def test_patch_treatment(self):

        treatment1 = Treatment.objects.get(name="John's treatment")

        body = OrderedDict(
            name = "Peter's treatment",
            beneficiary = "Peter"
        )

        url = self.treatment_url + str(treatment1.uuid)

        response = self.client.patch(
            url,
            body,
            format="json"
            )
        
        expected_data = {
            'uuid': str(treatment1.uuid),
            'associated_user': treatment1.associated_user.uuid,
            'name': "Peter's treatment",
            'beneficiary': "Peter"
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
    
    def test_put_treatment(self):

        treatment1 = Treatment.objects.get(name="John's treatment")

        body = OrderedDict(
            uuid = treatment1.uuid,
            associated_user = treatment1.associated_user.uuid,
            name = "Peter's treatment",
            beneficiary = "Peter"
        )

        url = self.treatment_url + str(treatment1.uuid)

        response = self.client.put(
            url,
            body,
            format="json"
            )
        
        expected_data = {
            'uuid': str(treatment1.uuid),
            'associated_user': treatment1.associated_user.uuid,
            'name': "Peter's treatment",
            'beneficiary': "Peter"
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_destroy_treatment(self):

        treatment1 = Treatment.objects.get(name="John's treatment")
        url = self.treatment_url + str(treatment1.uuid)

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
