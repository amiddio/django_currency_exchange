from django.test import TestCase
from app_exchange.forms import ExchangeForm


class ExchangeFormTest(TestCase):

    def test_amount_field_label(self):
        form = ExchangeForm()
        self.assertTrue(form.fields['amount'].label == 'Amount')

    def test_from_field_label(self):
        form = ExchangeForm()
        self.assertTrue(form.fields['currency_from'].label == 'From')

    def test_to_field_label(self):
        form = ExchangeForm()
        self.assertTrue(form.fields['currency_to'].label == 'To')

    def test_form_is_valid(self):
        form_data = {
            'amount': 10,
            'currency_from': 'USD',
            'currency_to': 'EUR',
        }
        form = ExchangeForm(data=form_data)
        self.assertTrue(form.is_valid())
