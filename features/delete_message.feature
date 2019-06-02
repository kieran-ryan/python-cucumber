# requires @compose_message

Feature: Delete Message

    @delete_message
    Scenario: Log in to Gmail, compose message, delete message
        Given user successfully logs in with valid username "username" and valid password "valid_password" and is on the inbox page
        When user deletes the message
        Then the message is successfully deleted
