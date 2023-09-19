from django import forms
from app_exchange.services.exchange import get_currency_code_list


class ExchangeForm(forms.Form):
    """Форма обмена валют"""

    CODE_LIST = get_currency_code_list()

    amount = forms.IntegerField(label='Amount', min_value=1, max_value=1000000)
    currency_from = forms.ChoiceField(label='From', choices=CODE_LIST)
    currency_to = forms.ChoiceField(label='To', choices=CODE_LIST)

