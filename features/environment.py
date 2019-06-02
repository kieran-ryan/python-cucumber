from features.browser import Browser
from features.pages.login_page import LoginPage
from features.pages.inbox_page import InboxPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.inbox_page = InboxPage()


def after_all(context):
    context.browser.close()
