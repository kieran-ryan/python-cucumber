from nose.tools import assert_true
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.browser import Browser


class InboxPageElements(object):

    # inbox url
    INBOX_PAGE = 'https://mail.google.com/mail/u/0/#inbox'

    # navbar elements
    ACCOUNT_BUTTON = '#gb > div.gb_pd.gb_Fd.gb_xd.gb_5b > div.gb_wc.gb_Ka.gb_vc.gb_Dd > div > div.gb_Fa.gb_Qc.gb_bg.gb_f.gb_kf > div > a'
    LOGOUT_BUTTON = '#gb_71'

    # compose message elements
    COMPOSE = '//div[text()="Compose"]'
    RECIPIENT = '//textarea[@aria-label="To"]'
    SUBJECT = '//input[@aria-label="Subject"]'
    MESSAGE = '//div[@aria-label="Message Body"]'
    SEND = '//div[@aria-label="Send ‪(⌘Enter)‬"]'

    # message options
    DELETE = '//*[@id=":4"]/div/div[1]/div[1]/div/div/div[2]/div[3]/div'
    # the notification that appears when a message is deleted
    DELETE_SUCCESS = '//span[contains(text(), "Conversation moved to Trash."]'
    MOVE_TO = '//*[@aria-label="Move to"]'
    MOVE_TO_MENU_OPEN = '//input[@aria-label="Move-to menu open"]'
    MESSAGE_SELECT = '//div[@role="checkbox"]'

    # search and filter elements
    SEARCH = '#aso_search_form_anchor > div > input'
    RESULT = '// *[ @ id = "link_vsm"]'


class InboxPage(Browser):
    # inbox actions

    def navigate_to_inbox(self):
        self.driver.get(InboxPageElements.INBOX_PAGE)

    def assert_login_success(self):
        # if account button is present we have logged in
        assert_true(self.driver.find_element_by_xpath(InboxPageElements.ACCOUNT_BUTTON))

    def get_page_title(self):
        return self.driver.title

    def message_sent_assert(self):
        view_message_link = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, InboxPageElements.RESULT))
        )
        view_message_link.click()

    def select_message(self):
        select_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, InboxPageElements.MESSAGE_SELECT))
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

    def filter_result(self):
        self.select_message()

    def delete_message(self):
        WebDriverWait(self.driver, 1000)
        self.select_message()
        self.driver.find_element_by_xpath(InboxPageElements.DELETE).click()

    def delete_success(self):
        self.driver.find_element_by_css_selector(InboxPageElements.DELETE_SUCCESS)

    def move_message_to_folder(self, folder_name):
        WebDriverWait(self.driver, 1000)

        self.select_message()

        wait_for_folder_dropdown = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, InboxPageElements.MOVE_TO))
        )
        wait_for_folder_dropdown.click()

        actions = ActionChains(self.driver)
        actions.send_keys(folder_name)
        actions.perform()

        self.driver.find_element_by_xpath('//span[contains(text(), "Test Folder"]').click()

    def assert_message_moved(self, folder_name):
        self.driver.find_element_by_xpath('//span[@title="' + folder_name + '"]').click()
        self.delete_message()

    def logout(self):
        account_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, InboxPageElements.ACCOUNT_BUTTON))
        )
        account_button.click()

        self.driver.find_element_by_css_selector(InboxPageElements.LOGOUT_BUTTON).click()
