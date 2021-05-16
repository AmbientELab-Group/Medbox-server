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
        
        self.treatment1 = Treatment.objects.create(
            associated_user = self.owner,
            name = "John's treatment",
            beneficiary = "John"
        )

    def test_get_all_treatments(self):
        # get api response
        
       

        temp = OrderedDict(
                    uuid = str(self.treatment1.uuid),
                    associated_user = UUID(str(self.treatment1.associated_user.uuid)),
                    name = self.treatment1.name,
                    beneficiary = self.treatment1.beneficiary
                    )
        
        #print(temp)

        expected_data = [temp]
        
        #print(Treatment.beneficiary) /api/treatments/?beneficiary=benef1
        response = self.client.get(self.treatment_url, {"beneficiary": self.treatment1.beneficiary})
        #response = self.client.get("/api/treatments/?beneficiary=John")
        #print(f"""****\ncode: {response.status_code}\nresponse: {response.data}\n expected: {expected_data}\n****""")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
"""  
    def test_get_single_treatment(self):
       
        expected_data = {
            "uuid": str(self.treatments[0].uuid),
            "associated_user" : self.treatments[0].associated_user,
            "name" : self.treatments[0].name,
            "beneficiary" : self.treatments[0].beneficiary
        }

        print(expected_data)
        print("---------------------------------")
        response = self.client.get(self.treatment_url + f"?treatment={self.treatments[0].uuid}")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data, expected_data)
   
   def test_create_treatment(self):

        input_data = OrderedDict(
                name = "peter's treatment",
                beneficiary = "peter"
                )
        
        response = self.client.post(
            self.treatment_url, 
            input_data,
            format="json"
            )
        
        test_data = OrderedDict(
            uuid = Treatment.uuid,
            associated_user = str(Treatment.associated_user),
            name = "peter's treatment",
            beneficiary = "peter"
        )
        
        test_data = {
            "uuid": str(self.treatments.uuid),
            "associated_user" : self.treatments.associated_user,
            "name" : self.treatments.name,
            "beneficiaary" : self.treatments.beneficiary
        }

        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data, test_data)
    
    def test_update_treatment(self):

        test_data = OrderedDict(
            uuid = Treatment.uuid,
            associated_user = str(Treatment.associated_user),
            name = "peter's treatment",
            beneficiary = "peter"
        )
        updated_data = OrderedDict(
                name = "peter's treatment",
                beneficiary = "peter"
        )

        response = self.client.put(
            self.treatment_url + f"/{self.treatments[0].uuid}",
            updated_data,
            format="json"
            )
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, test_data)
     
    def test_destroy_treatment(self): 
        test_data = OrderedDict(
            uuid = Treatment.uuid,
            associated_user = str(Treatment.associated_user),
            name = "peter's treatment",
            beneficiary = "peter"
        )

        response = self.client.delete(self.treatment_url + f"/{self.treatments[0].uuid}")
        print(response)
        final_treatment = Treatment.objects.filter(
            uuid = self.treatments[0].uuid
        )
        serializer = TreatmentSerializer(final_treatment, many=True)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(serializer.data, expected_containers)
        """