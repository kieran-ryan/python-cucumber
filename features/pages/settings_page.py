from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.browser import Browser


class SettingsPageElements(object):

    # folder elements
    ADD_FOLDER = '#\:qx'
    FOLDER_NAME = '#\:pt\.na'
    FOLDER_SUBMIT = 'body > div.Kj-JD > div.Kj-JD-Jl > button.J-at1-auR'
    FOLDER_SUCCESS = 'body > div:nth-child(18) > div.nH > div > div.nH.w-asV.aiw > div:nth-child(6) > div.no > div > div:nth-child(3) > div > div > div.vh > span > span'

    # settings elements
    SETTINGS_TITLE = '#\:4 > div > div.nH.qZ.G-atb > div.du > h2'
    SETTINGS_LINK = 'https://mail.google.com/mail/u/0/#settings/labels'


class SettingsPage(Browser):

    def navigate_to_settings(self):
        self.driver.get(SettingsPageElements.SETTINGS_LINK)

    def create_folder(self, name):
        create_folder_button = self.driver.find_element_by_css_selector(SettingsPageElements.ADD_FOLDER)
        create_folder_button.click()

        self.driver.find_element_by_css_selector(SettingsPageElements.FOLDER_NAME).send_keys(name)
        self.driver.find_element_by_xpath(SettingsPageElements.FOLDER_SUBMIT).click()

    def folder_success(self):
        self.driver.find_element_by_css_selector(SettingsPageElements.FOLDER_SUCCESS)

