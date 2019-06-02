from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.browser import Browser


class InboxPageElements(object):
    # inbox page elements

    # navbar elements
    ACCOUNT_BUTTON = '#gb > div.gb_pd.gb_Fd.gb_xd.gb_5b > div.gb_wc.gb_Ka.gb_vc.gb_Dd > div > div.gb_Fa.gb_Qc.gb_bg.gb_f.gb_kf > div > a'
    LOGOUT_BUTTON = '#gb_71'
    LOGOUT_LINK = 'https://accounts.google.com/Logout'

    # message elements
    SELECT_MESSAGE = '#\:c8'
    DELETE = '#\:4 > div > div.nH.aqK > div.Cq.aqL > div > div > div:nth-child(2) > div.T-I.J-J5-Ji.nX.T-I-ax7.T-I-Js-Gs.mA > div'
    COMPOSE = '//div[text()="Compose"]'
    RECIPIENT = '#\:87'
    SUBJECT = '#\:7p'
    MESSAGE = '#\:8u'
    SEND = '#\:7f'


class InboxPage(Browser):
    # inbox actions

    def get_page_title(self):
        return self.driver.title

    def compose_message(self, recipient, subject, message):
        compose_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, InboxPageElements.COMPOSE))
        )
        compose_button.click()

        self.driver.find_element_by_css_selector(InboxPageElements.RECIPIENT).send_keys(recipient)
        self.driver.find_element_by_css_selector(InboxPageElements.SUBJECT).send_keys(subject)
        self.driver.find_element_by_css_selector(InboxPageElements.MESSAGE).send_keys(message)

    def send_message(self):
        self.driver.find_element_by_css_selector(InboxPageElements.SEND).click()

    def delete_message(self):
        self.driver.find_element_by_css_selector(InboxPageElements.SELECT_MESSAGE).click()
        self.driver.find_element_by_css_selector(InboxPageElements.DELETE).click()

    def logout(self):
        account_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, InboxPageElements.ACCOUNT_BUTTON))
        )
        account_button.click()

        self.driver.find_element_by_css_selector(InboxPageElements.LOGOUT_BUTTON).click()
