from behave import *


@step('user navigates to the settings page')
def step_impl(context):
    context.settings_page.navigate_to_settings()


@when('user adds a folder with name "{folder_name}"')
def step_impl(context, folder_name):
    context.settings_page.create_folder(folder_name)


@when('user selects a message by message subject "{message_subject}" to move to "{folder_name}"')
def step_impl(context, message_subject, folder_name):
    context.inbox_page.move_message_to_folder(message_subject, folder_name)


@then('a folder is successfully created')
def step_impl(context):
    context.settings_page.folder_success()
