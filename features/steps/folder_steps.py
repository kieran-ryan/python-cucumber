from behave import *
from nose.tools import assert_equal, assert_true


@step('user navigates to the settings page')
def step_impl(context):
    context.settings_page.navigate_to_settings()


@when('user adds a folder with name "{folder_name}"')
def step_impl(context, folder_name):
    context.settings_page.create_folder(folder_name)


@then('a folder "{folder_name}" is successfully created')
def step_impl(context, folder_name):
    assert_equal(context.inbox_page.get_page_title(), folder_name)


@given('user selects a message to move to "{folder_name}"')
def step_impl(context, folder_name):
    context.inbox_page.move_message_to_folder(folder_name)
