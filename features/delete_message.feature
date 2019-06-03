# requires @compose_message

Feature: Delete Message

    @delete_message
    Scenario: Log in to Gmail, compose message, delete message
        Given user successfully logs in with valid username "username" and valid password "valid_password" and is on the inbox page
        And user composes a message with recipient "recipient@recipient's_email.com" and subject "Test Subject" and message "Test Message"
        When user deletes the message
        Then the message is successfully deleted
