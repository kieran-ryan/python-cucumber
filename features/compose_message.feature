Feature: Compose Message

    @compose_message
    Scenario: Log in to Gmail and compose message
        Given user successfully logs in with valid username "username" and valid password "valid_password" and is on the inbox page
        When user composes a message with recipient "recipient@recipient's_email.com" and subject "Test Subject" and message "Test Message"
        And user sends message
        Then the message is sent successfully