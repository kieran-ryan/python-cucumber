Feature: Delete Message

    @delete_message
    Scenario: Log in to Gmail, compose message, delete message
        Given user is on the inbox page
#        And user composes a message with recipient "recipient@recipient's_email.com" and subject "Delete Me" and message "Delete Me Message"
#        And user sends message
        When user deletes the message
        Then the message is successfully deleted
