import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utilities import get_base_url


class GfnParser(object):
    FIELD_EMAIL_LOCATOR = (By.ID, 'username')
    FIELD_PASSWORD_LOCATOR = (By.ID, 'password')
    BUTTON_LOGIN_LOCATOR = (By.CSS_SELECTOR, 'button.btn:nth-child(1)')
    HOME_OFFICE_BUTTON_LOCATOR = (By.ID, 'flexRadioDefault1')
    START_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'input.btn')
    END_BUTTON_LOCATOR = (By.XPATH, "//*[text()='Beenden']")


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = get_base_url()

    def element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def navigate_to_main(self):
        self.driver.get(self.base_url)

    @property
    def _field_email(self):
        return self.element(GfnParser.FIELD_EMAIL_LOCATOR)

    @property
    def _field_password(self):
        return self.element(GfnParser.FIELD_PASSWORD_LOCATOR)

    @property
    def _button_login(self):
        return self.element(GfnParser.BUTTON_LOGIN_LOCATOR)

    @property
    def _home_office_button(self):
        return self.element(GfnParser.HOME_OFFICE_BUTTON_LOCATOR)

    @property
    def _time_start_button(self):
        return self.element(GfnParser.START_BUTTON_LOCATOR)

    @property
    def _time_end_button(self):
        return self.element(GfnParser.END_BUTTON_LOCATOR)

    def _enter_email(self, email: str):
        self._field_email.send_keys(email)

    def _enter_password(self, password: str):
        self._field_password.send_keys(password)

    def _click_login_button(self):
        self._button_login.click()

    def account_login(self, email: str, password: str):
        self._enter_email(email)
        self._enter_password(password)
        self._click_login_button()

    def _choose_home_office(self):
        self._home_office_button.click()

    def _start_time_button(self):
        self._time_start_button.click()

    def _end_time(self):
        self._time_end_button.click()

    def start_time(self, email: str, password: str):
        self.navigate_to_main()
        self.account_login(email, password)
        self.handle_website_alert()
        self._choose_home_office()
        self._start_time_button()

        time.sleep(2)


    def handle_website_alert(self):
        # Example: Handle alert by accepting it
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass  # No alert found

    def end_time(self, email: str, password: str):
        self.navigate_to_main()
        self.account_login(email, password)
        if self.element_is_visible(GfnParser.END_BUTTON_LOCATOR):
            self._end_time()
        else:
            print('Heute kein Unterricht!')
        time.sleep(2)


    def element_is_visible(self, locator, timeout=2):
        try:
            WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))
            is_visible = True
        except TimeoutException:
            is_visible = False
        return is_visible

    def __del__(self):
        self.driver.quit()