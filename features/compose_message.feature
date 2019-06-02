Feature: Compose Message

    @message
    Scenario: Log in to Gmail and compose message
        Given user is on the login page
        When user enters valid username "username" and valid password "valid_password"
        And user is on the inbox page
        When user clicks on the compose button
        And user composes a message
        And user sends message
        Then the message is sent successfully