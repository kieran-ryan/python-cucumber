from behave import *
from nose.tools import assert_equal, assert_true


# if title is 'Inbox' then user is on the inbox page
@step('user is on the inbox page')
def step_impl(context):
    context.inbox_page.navigate_to_inbox()
    # assert_equal(context.inbox_page.get_page_title(), 'Gmail')


# execute login steps to get to inbox page
@given('user successfully logs in with valid '
       'username "{username}" and '
       'valid password "{password}" and '
       'is on the inbox page')
def step_impl(context, username, password):
    context.execute_steps(u'''given user is on the login page''')
    context.login_page.login(username, password)


@step('user composes a message with '
      'recipient "{recipient}" and '
      'subject "{subject}" and '
      'message "{message}"'
      )
def step_impl(context, recipient, subject, message):
    context.inbox_page.compose_message(recipient, subject, message)


@step('user sends message')
def step_impl(context):
    context.inbox_page.send_message()


@step('the message is sent successfully')
def step_impl(context):
    context.inbox_page.message_sent_assert()


@when('user deletes the message by message subject "{message_subject}"')
def step_impl(context, message_subject):
    context.inbox_page.delete_message(message_subject)


@then('the message is successfully deleted')
def step_impl(context):
    assert_true(context.inbox_page.delete_success)


@when('user searches for a message with search term "{search_term}"')
def step_impl(context, search_term):
    context.inbox_page.search_for_message(search_term)


@then('the message results are filtered by search term "{message_subject}"')
def step_impl(context, message_subject):
    context.inbox_page.filter_result(message_subject)


@then('the message is successfully moved to folder "{folder_name}"')
def step_impl(context, folder_name):
    context.inbox_page.assert_message_moved(folder_name)
