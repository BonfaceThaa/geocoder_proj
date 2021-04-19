import unittest
from django.test import Client


class GetWardTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_reverse_geolocation(self):
        response = self.client.get('/api/v1/wards/get_admin/', {'lat': 1.4388, 'long': 37.0834})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['features'][0]['properties']['gid'], 675)

    def test_get_reverse_geolocation_bad_request(self):
        response = self.client.get('/api/v1/wards/get_admin/', {})
        self.assertEqual(response.status_code, 400)


