Feature: Folders

    @new_folder
    Scenario: Log in to Gmail and add a folder from the settings page
        Given user successfully logs in with valid username "username" and valid password "valid_password" and is on the inbox page
        And user navigates to the settings page
        When user adds a folder with name "Test Folder"
        Then a folder "Test Folder" is successfully created

    Scenario: Move message to folder
        Given user selects a message to move to "Test Folder"
        When move to "Test Folder" is selected
        Then the message is successfully moved
