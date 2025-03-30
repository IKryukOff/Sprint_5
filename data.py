import random
import string


class Urls:
    main_page = 'https://stellarburgers.nomoreparties.site/'
    registration_page = 'https://stellarburgers.nomoreparties.site/register'
    login_page = 'https://stellarburgers.nomoreparties.site/login'
    profile_page = 'https://stellarburgers.nomoreparties.site/account/profile'
    order_history_page = 'https://stellarburgers.nomoreparties.site/account/order-history'
    forgot_password_page = 'https://stellarburgers.nomoreparties.site/forgot-password'


class User:
    login = 'ivanivanov2025@ya.ru'
    password = 'ivanpassword'

    def __init__(self, name: str, login: str, password: str) -> None:
        self.name = name
        self.login = login
        self.password = password

    @classmethod
    def generate(cls):
        return cls(name='Random User',
                   login=f'randomuser{random.randint(100, 999)}@ya.ru',
                   password=''.join(random.choices(string.ascii_letters + string.digits, k=6)))
