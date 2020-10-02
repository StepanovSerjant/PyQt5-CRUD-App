from email_validator import validate_email, EmailNotValidError
from sqlalchemy.exc import IntegrityError

from database.db import create_user, session, get_user_info, user_exist
import settings


def email_validation(email):
    """ Функция валидации почтового адреса """
    try:
        valid = validate_email(email)
        email = valid.email
        return True
    except EmailNotValidError as e:
        return False


def validate_password(password):
    """ Проверка наличия недопустимых символов в пароле """
    PASS_INVALID_CHARACTERS = (
        '!', '№', ';', '%', ':', '?', '*', '(', ')',
        '_', '+', '-', '!', '@', '#', '$', '^', '&',
        '*', '[', ']', '{', '}', ' '
    )
    for character in PASS_INVALID_CHARACTERS:
        if character in password:
            return False
    return True


def validate_len(data):
    """ Проверка соответствия данных указанной длине """
    invalid_len = []
    for key in data:
        try:
            if len(data[key][0]) > int(data[key][1]):
                invalid_len.append(key)
        except IndexError:
            pass
    return invalid_len


def check_fullness(data: dict, check_len=False):
    """ Функция проверки заполненности данных """
    if check_len == True:
        invalid_len = validate_len(data)
        if invalid_len:
            return {'type': 'len', 'data': invalid_len}
    empty_fields = [key for key in data if len(str(data[key][0])) == 0]
    if empty_fields:
        return {'type': 'empty', 'data': empty_fields}
    return None


def invalid_info(invalid_fields):
    """ Функция генерирующая сообщение о не заполненных данных """
    result = {'status': False}
    if len(invalid_fields['data']) == 1:
        fields = invalid_fields['data'][0]
        result['message'] = f'У вас не заполнено поле {fields}.'
        if invalid_fields['type'] == 'len':
            result['message'] = f'Превышена допустимая длина для поля: {fields}.'
    else:
        fields = ', '.join([field for field in invalid_fields['data']])
        result['message'] = f'У вас не заполнены следующие поля: {fields}.'
        if invalid_fields['type'] == 'len':
            result['message'] = f'Превышена допустимая длина для полей: {fields}.'
    return result


def user_auth(user_data):
    """ Функция авторизации """
    is_full = check_fullness(user_data)
    if is_full != None:
        return invalid_info(is_full)
    if not user_exist(user_data['name']):
        return {'status': False, 'message': 'Не существует профиля с таким именем.'}
    elif get_user_info(user_data['name']).password != user_data['password']:
        return {'status': False, 'message': 'Неверный пароль.'}
    else:
        return {'status': True, 'message': 'Авторизация прошла успешно.'}


def user_registration(register_data):
    """ Функция обработки регистрационных данных """
    is_full = check_fullness(register_data, check_len=True)
    if is_full != None:
        return invalid_info(is_full)
    elif not email_validation(register_data['email'][0]):
        return {'status': False, 'message': 'Укажите реальный email адрес.'}
    elif not validate_password(register_data['pass'][0]):
        return {'status': False, 'message': 'Пароль содержит недопустимые символы.'}
    elif register_data['pass'][0] != register_data['pass_confirm']:
        return {'status': False, 'message': 'Неверный пароль подверждения.'}
    else:
        try:
            create_user(
                name=register_data['username'][0],
                password=register_data['pass'][0],
                email=register_data['email'][0]
            )  
        except IntegrityError as error:
            session.rollback()
            if 'email' in str(error).split('.')[2]:
                return {'status': False, 'message': 'На одной почте у вас может быть только один аккаунт.'}
            return {'status': False, 'message': 'Пользователь с таким именем уже существует.'}
        else:
            return {'status': True, 'message': 'Регистрация прошла успешно.'}


def create_wish(adding_data):
    """ Функция обработки данных при добавлении нового желания """
    is_full = check_fullness(adding_data, check_len=True)
    if is_full != None:
        return invalid_info(is_full)
    else:
        return {'status': True, 'message': 'Добавление нового желания прошло успешно.'}
