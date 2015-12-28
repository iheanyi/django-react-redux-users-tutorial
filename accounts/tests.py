from django.core.urlresolvers import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status

class AccountsTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user. 
        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        # URL for creating an account.
        self.create_url = reverse('account-create')

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }

        response = self.client.post(url , data, format='json')
        user = User.objects.latest('id')
        #token = Token.objects.get(user=user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        #self.assertEqual(response.data['token'], token.key)
        self.assertFalse(response.data['password'] in response.data)
