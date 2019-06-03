from features.browser import Browser
from features.pages.login_page import LoginPage
from features.pages.inbox_page import InboxPage
from features.pages.settings_page import SettingsPage


def before_all(context):

    # user credentials
    username = 'username'
    password = 'password'

    context.browser = Browser()
    context.login_page = LoginPage()
    context.inbox_page = InboxPage()
    context.settings_page = SettingsPage()

    context.login_page.navigate_to_gmail()
    context.login_page.login(username, password)


def after_all(context):
    context.browser.close()
