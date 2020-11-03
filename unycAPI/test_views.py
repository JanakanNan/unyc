from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from unycAPI.views import *

class BieresTests(APITestCase):
    def test_list_bieres(self):
        """
        Ensure we can create a new account object.
        """
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        response = self.client.get(reverse('ListBieres.'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

