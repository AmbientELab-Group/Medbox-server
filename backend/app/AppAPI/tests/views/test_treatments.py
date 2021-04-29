
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

    TreatmentUrl = "/api/treatments"

    def setUp(self):

        self.user = get_user_model().objects.create(
            email="testemail@test.com",
            password="testpassword"
        )

        tokens = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION="bearer " + str(tokens.access_token)
        )

        self.client.credentials(HTTP_AUTHORIZATION="bearer " + str(tokens.access_token))
        
        self.treatments = []

        for i in range(3):
            self.treatments.append(
                Treatment.objects.create(
                    associated_user = self.user,
                    name = "John's treatment",
                    beneficiary = "John"
                )
            )

    def test_get_all_treatments(self):
        # get api response
        response = self.client.get(self.TreatmentUrl)
        treatments = Treatment.objects.all()
        serializer = TreatmentSerializer(treatments, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

        for treatment in self.treatments:

            self.assertIn(
                TreatmentSerializer(instance=treatement).data,
                repsonse.data
            )
    
    def test_get_single_treatment(self):
        expected_data = OrderedDict(
            associated_user = self.treatments[0].associated_user,
            name = self.treatments[0].name,
            beneficiary = self.treatments[0].beneficiary
            )

        response = self.client.get(self.TreatmentUrl + f"{self.treatments[0].uuid}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expect_data)
        
    def test_create_treatment(self):

        input_data = OrderedDict(
                associated_user = self.treatments[0].associated_user,
                name = self.treatments[0].name,
                beneficiary = self.treatments[0].beneficiary
                )

        response = self.client.post(self.TreatmentUrl, input_data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data, input_data)
    
    def test_update_treatment(self):

        expected_data = OrderedDict(
            associated_user = self.treatments[0].associated_user,
            name = self.treatments[0].name,
            beneficiary = self.treatments[0].beneficiary
        )

        updated_data = OrderedDict(
            associated_user = self.treatments[0].associated_user,
            name = self.treatments[0].name,
            beneficiary = self.treatments[0].beneficiary
        )

        response = self.client.put(
            self.TreatmentUrl + f"{self.treatments[0].uuid}",
            updated_data
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, updated_data)

   
    def test_destroy_treatment(self):
        input_data = OrderedDict(
            associated_user = self.treatments[0].associated_user,
            name = self.treatments[0].name,
            beneficiary = self.treatments[0].beneficiary
            )

        response = self.client.delete(self.TreatmentUrl + f"/{self.treatments[0].uuid}")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(treatment.objects.filter(pk=self.treatement.id))
