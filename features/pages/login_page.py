from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.browser import Browser


class LoginPageElements(object):

    BODY = '#yDmH0d'
    USER = 'identifierId'
    USER_SUBMIT = '#identifierNext > content > span'
    PASS = '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'
    SUBMIT = '#passwordNext > content > span'
    ERROR = '#password > div.LXRPh > div.dEOOab.RxsGPe'


class LoginPage(Browser):
    # login page actions

    def navigate_to_gmail(self):
        self.driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&continue='
                        'https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin#identifier')

    def get_page_title(self):
        return self.driver.title

    def get_login_error(self):
        return self.driver.find_element_by_css_selector(LoginPageElements.ERROR)

    def set_username(self, username):
        user_name_field = self.driver.find_element_by_id(LoginPageElements.USER)
        user_name_field.send_keys(username)
        self.driver.find_element_by_css_selector(LoginPageElements.USER_SUBMIT).click()

    def set_password(self, password):
        password_field = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LoginPageElements.PASS))
        )
        password_field.send_keys(password)

    def submit_login(self):
        self.driver.find_element_by_css_selector(LoginPageElements.SUBMIT).click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.submit_login()
