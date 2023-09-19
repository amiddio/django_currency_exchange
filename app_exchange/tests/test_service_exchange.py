from django.test import TestCase
from app_exchange.services.exchange import _get_currencies, _get_rates, get_currency_code_list, get_exchange_result


class ServiceExchangeTest(TestCase):

    def test_get_currency_code_list_method(self):
        tpl = get_currency_code_list()
        self.assertIsInstance(tpl, tuple)
        self.assertGreater(len(tpl), 0)

    def test_get_exchange_result_method(self):
        result = get_exchange_result(
            amount=10,
            currency_code_from='USD',
            currency_code_to='EUR'
        )
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)

    def test__get_rates_method(self):
        rates = _get_rates()
        self.assertIsInstance(rates, dict)
        self.assertGreater(len(rates), 0)

    def test__get_currencies_method(self):
        responce = _get_currencies()
        self.assertEquals(responce.get('result'), 'success')
