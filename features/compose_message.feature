Feature: Compose Message

    @message
    Scenario: Log in to Gmail and compose message
        Given user is on the login page
        When user enters valid username "username" and valid password "valid_password"
        And user is on the inbox page
        And user composes a message with recipient "recipient@recipient's_email.com" and subject "Test Subject" and message "Test Message"
        And user sends message
        Then the message is sent successfully