from behave import *
from nose.tools import assert_equal, assert_true


# if title is 'Inbox' then user is on the inbox page
@step('user is on the inbox page')
def step_impl(context):
    assert_equal(context.inbox_page.get_page_title(), 'Gmail')


@when('user clicks on the compose button')
def step_impl(context):
    context.inbox_page.compose_message()

