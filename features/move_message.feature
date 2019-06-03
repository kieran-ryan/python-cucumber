Feature: Move Message

    @move_message
    Scenario: Move message to folder
        Given user successfully logs in with valid username "username" and valid password "valid_password" and is on the inbox page
        And user composes a message with recipient "recipient@recipient's_email.com" and subject "Test Subject" and message "Test Message"
        And user sends message
        And user navigates to the settings page
        When user adds a folder with name "Test Folder"
        And user is on the inbox page
        And user selects a message to move to "Test Folder"
        Then the message is successfully moved to folder "Test Folder"
