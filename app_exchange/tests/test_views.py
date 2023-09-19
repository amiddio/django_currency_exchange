from django.test import TestCase


class ExchangeViewTest(TestCase):

    def test_index_url_is_exists(self):
        responce = self.client.get('/')
        self.assertEqual(200, responce.status_code)
