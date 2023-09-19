from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from app_exchange.forms import ExchangeForm
from app_exchange.services.exchange import get_exchange_result
from app_exchange.utils import json_responce_success, json_responce_form_errors, json_responce_server_errors


class ExchangeView(View):
    """Представление формы"""

    def get(self, request):
        """Обработка get запроса"""
        form = ExchangeForm()
        return render(request, template_name='app_exchange/index.html', context={'form': form})

    def post(self, request):
        """Обработка post запроса"""
        if self._is_ajax(request):
            form = ExchangeForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                result = get_exchange_result(
                    amount=cd['amount'], currency_code_from=cd['currency_from'], currency_code_to=cd['currency_to']
                )
                return JsonResponse(json_responce_success(result=result), status=200)
            else:
                return JsonResponse(json_responce_form_errors(errors=form.errors), status=200)

        return JsonResponse(json_responce_server_errors(), status=200)

    def _is_ajax(self, request):
        """Проверяем метод запроса на ajax"""
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
