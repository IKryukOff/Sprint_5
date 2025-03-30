from selenium.webdriver.chrome.webdriver import WebDriver

from locators import MainPage


class TestConstructorSection:
    def test_click_buns_scroll_to_buns(self, login: WebDriver) -> None:
        driver = login
        driver.find_element(*MainPage.constructor_link_text).click()
        driver.find_element(*MainPage.fillings_tab).click()
        driver.find_element(*MainPage.buns_tab).click()
        h_buns = driver.find_element(*MainPage.h_buns)

        assert h_buns.text == 'Булки'

    def test_click_sauces_scroll_to_sauces(self, login: WebDriver) -> None:
        driver = login
        driver.find_element(*MainPage.constructor_link_text).click()
        driver.find_element(*MainPage.sauces_tab).click()
        h_sauces = driver.find_element(*MainPage.h_sauces)

        assert h_sauces.text == 'Соусы'

    def test_click_fillings_scroll_to_fillings(self, login: WebDriver) -> None:
        driver = login
        driver.find_element(*MainPage.constructor_link_text).click()
        driver.find_element(*MainPage.fillings_tab).click()
        h_fillings = driver.find_element(*MainPage.h_fillings)

        assert h_fillings.text == 'Начинки'
