Feature: Search and Filter Message

    @search_message
    Scenario: Log in to Gmail, search for message, assert filtered result
        Given user successfully logs in with valid username "username" and valid password "valid_password" and is on the inbox page
        When user searches for a message with search term "Test Subject"
        Then the message results are filtered
