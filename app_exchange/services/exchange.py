import requests

from app.settings import env
from typing import Optional


def get_currency_code_list() -> tuple:
    """Кортеж с кодами валют. Используется в select элементах формы"""
    rates = _get_rates()
    if rates:
        return tuple((k, k) for k in rates.keys())

    return tuple()


def get_exchange_result(amount: int, currency_code_from: str, currency_code_to: str) -> float:
    """Происходит калькуляция валют"""
    rates = _get_rates()
    if rates:
        val_from = float(rates.get(currency_code_from))
        val_to = float(rates.get(currency_code_to))
        return round((val_to / val_from) * float(amount), 3)

    return 0.0


def _get_rates() -> Optional[dict]:
    """Получаем словарь валют, где ключем является код валюты, а значением курс к доллару"""
    response = _get_currencies()
    if response.get('result') == 'success':
        return response.get('conversion_rates', None)


def _get_currencies() -> dict:
    """Достаем словарь с данными валют из внешнего сервиса"""
    response = requests.get(env('EXCHANGE_API')).json()
    if response.get('result') == 'error':
        return dict()

    return response
