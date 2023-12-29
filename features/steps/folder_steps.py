from behave import *


@step('user navigates to the settings page')
def step_impl(context):
    context.settings_page.navigate_to_settings()


@when('user adds a folder with name "{}"')
def step_impl(context, folder_name):
    context.settings_page.create_folder(folder_name)


@step('user selects a message to move to "{}"')
def step_impl(context, folder_name):
    context.inbox_page.move_message_to_folder(folder_name)


@then('a folder is successfully created')
def step_impl(context):
    context.settings_page.folder_success()
    context.inbox_page.navigate_to_inbox()


@then('the message is successfully moved to folder "{}"')
def step_impl(context, folder_name):
    context.inbox_page.assert_message_moved(folder_name)
