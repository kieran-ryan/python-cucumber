from behave import *
from nose.tools import assert_equal, assert_true


# if title is 'Inbox' then user is on the inbox page
@step('user is on the inbox page')
def step_impl(context):
    assert_equal(context.inbox_page.get_page_title(), 'Gmail')


@step('user composes a message with '
      'recipient "{recipient}" and '
      'subject "{subject}" and '
      'message "{message}"')
def step_impl(context, recipient, subject, message):
    context.inbox_page.compose_message(recipient, subject, message)


@step('user sends message')
def step_impl(context):
    context.inbox_page.send_message()

