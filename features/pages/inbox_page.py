from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.browser import Browser


class InboxPageElements(object):

    # navbar elements
    ACCOUNT_BUTTON = '#gb > div.gb_pd.gb_Fd.gb_xd.gb_5b > div.gb_wc.gb_Ka.gb_vc.gb_Dd > div > div.gb_Fa.gb_Qc.gb_bg.gb_f.gb_kf > div > a'
    LOGOUT_BUTTON = '#gb_71'

    # message elements
    DELETE = '//*[@id=":4"]/div/div[1]/div[1]/div/div/div[2]/div[3]/div'
    DELETE_SUCCESS = 'body > div:nth-child(18) > div.nH > div > div.nH.w-asV.aiw > div:nth-child(6) > div.no > div > div:nth-child(3) > div > div > div.vh > span'
    COMPOSE = '//div[text()="Compose"]'
    RECIPIENT = '//textarea[@aria-label="To"]'
    SUBJECT = '//input[@aria-label="Subject"]'
    MESSAGE = '//div[@aria-label="Message Body"]'
    SEND = '//div[@aria-label="Send ‪(⌘Enter)‬"]'
    MOVE_TO = '//*[contains(text(), "Move to")]'
    MESSAGE_SELECT = '//*[@span]' # '//*[contains(text(),"Test Subject")]'

    # search and filter elements
    SEARCH = '#aso_search_form_anchor > div > input'
    RESULT = '// *[ @ id = "link_vsm"]'


class InboxPage(Browser):
    # inbox actions

    def get_page_title(self):
        return self.driver.title

    def message_sent_assert(self):
        view_message_link = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, InboxPageElements.RESULT))
        )
        view_message_link.click()
        # self.driver.find_element_by_xpath(InboxPageElements.RESULT).click()

    def select_message(self, message_subject):
        select_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(),' + message_subject + ')]'))
        )
        select_button.click()

    def compose_message(self, recipient, subject, message):
        compose_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, InboxPageElements.COMPOSE))
        )
        compose_button.click()

        self.driver.find_element_by_xpath(InboxPageElements.RECIPIENT).send_keys(recipient)
        self.driver.find_element_by_xpath(InboxPageElements.SUBJECT).send_keys(subject)
        self.driver.find_element_by_xpath(InboxPageElements.MESSAGE).send_keys(message)

    def send_message(self):
        self.driver.find_element_by_xpath(InboxPageElements.SEND).click()

    def search_for_message(self, search_term):
        search = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, InboxPageElements.SEARCH))
        )
        search.send_keys(search_term)
        search.send_keys(Keys.ENTER)

    def filter_result(self, message_subject):
        self.select_message(message_subject)

    def delete_message(self, message_subject):
        self.select_message(message_subject)
        self.driver.find_element_by_xpath(InboxPageElements.DELETE).click()

    def delete_success(self):
        self.driver.find_element_by_css_selector(InboxPageElements.DELETE_SUCCESS)

    def move_message_to_folder(self, message_subject, folder_name):
        self.select_message(message_subject)
        self.driver.find_element_by_xpath(InboxPageElements.MOVE_TO).click()

        actions = ActionChains(self.driver)
        actions.send_keys(folder_name)
        actions.perform()

    def logout(self):
        account_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, InboxPageElements.ACCOUNT_BUTTON))
        )
        account_button.click()

        self.driver.find_element_by_css_selector(InboxPageElements.LOGOUT_BUTTON).click()
