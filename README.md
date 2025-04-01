# Sprint 5. UI-тестирование

UI-тестирование сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/)
1. Основа для написания автотестов — фреймворк pytest.
2. Перед запуском тестов установить зависимости — `pip install -r requirements.txt`.
3. Команда для запуска — `pytest -v`. 

## [Регистрация](tests/test_registration_page.py)
* `test_input_correct_creds_successful_registration` - При успешной регистрации перебрасывает на страницу входа
* `test_input_empty_name_nothing_happens` - При пустом поле "Имя" ничего не происходит: ни ошибки ни перехода на другую страницу
* `test_input_incorrect_email_user_exists_error` - При некорректном "email" появляется ошибка "Такой пользователь уже существует"
* `test_input_incorrect_password_less_six_symbols_password_error` - При некорректном "password" (менее 6 символов) появляется ошибка "Некорректный пароль"
## [Авторизация](tests/test_login_page.py)
* `test_login_via_login_button_show_main_page` - Вход по кнопке "Войти в аккаунт" на главной
* `test_login_via_profile_show_main_page` - Вход через кнопку "Личный кабинет"
* `test_login_via_registration_page_show_main_page` - Вход через кнопку в форме регистрации
* `test_login_via_forgot_password_page_show_main_page` - Вход через кнопку в форме восстановления пароля
## [Личный кабинет](tests/test_profile_page.py)
* `test_click_profile_link_open_profile_page_with_order_history` - Отображение "Личного кабинета"
* `test_click_constructor_link_show_constructor` - Переход из "Личного кабинета" в "Конструктор"
* `test_click_main_logo_show_constructor` - Переход из "Личного кабинета" в "Конструктор" при нажатии на логотип
* `test_click_logout_button_show_login_page` -  Выход из аккаунта
## [Раздел "Конструктор"](tests/test_constructor_section.py)
* `test_click_buns_scroll_to_buns` - Переход на "Булки"
* `test_click_sauces_scroll_to_sauces` - Переход на "Начинки"
* `test_click_fillings_scroll_to_fillings` - Переход на "Соусы"

