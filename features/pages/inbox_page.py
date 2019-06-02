from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.browser import Browser


class InboxPageElements(object):
    # inbox elements

    ACCOUNT_BUTTON = '#gb > div.gb_pd.gb_Fd.gb_xd.gb_5b > div.gb_wc.gb_Ka.gb_vc.gb_Dd > div > div.gb_Fa.gb_Qc.gb_bg.gb_f.gb_kf > div > a'
    LOGOUT_BUTTON = '#gb_71'
    LOGOUT_LINK = 'https://accounts.google.com/Logout'


class InboxPage(Browser):
    # inbox actions

    def get_page_title(self):
        return self.driver.title

    def logout(self):
        account_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, InboxPageElements.ACCOUNT_BUTTON))
        )
        account_button.click()

        self.driver.find_element_by_css_selector(InboxPageElements.LOGOUT_BUTTON).click()
