Feature: Search and Filter Message

    @search_message
    Scenario: Log in to Gmail, search for message, assert filtered result
        Given user successfully logs in with valid username "username" and valid password "valid_password" and is on the inbox page
        And user composes a message with recipient "recipient@recipient's_email.com" and subject "Test Subject" and message "Test Message"
        And user sends message
        When user searches for a message with search term "Test Subject"
        Then the message results are filtered by search term "Test Subject"
