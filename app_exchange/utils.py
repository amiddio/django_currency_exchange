import json


def json_responce_success(result: float) -> dict:
    """Успешный ответ с отправкой результата"""
    return {'success': True, 'result': result}


def json_responce_form_errors(errors) -> dict:
    """Отправка ошибок в форме"""
    return {'success': False, 'errors': errors.as_json()}


def json_responce_server_errors() -> dict:
    """Выводим общие ошибки которые возникают на сервере"""
    errors = json.dumps({
        'non_field_errors': [{"message": "Internal server error"}]}
    )
    return {'success': False, 'errors': errors}
