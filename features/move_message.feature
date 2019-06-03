Feature: Folders

    @move_message
    Scenario: Move message to folder
        Given user successfully logs in with valid username "username" and valid password "valid_password" and is on the inbox page
        When user selects a message by message subject "Test Subject" to move to "Test Folder"
        Then the message is successfully moved
