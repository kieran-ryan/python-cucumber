Feature: Folders

    @new_folder
    Scenario: Log in to Gmail and add a folder from the settings page
        Given user successfully logs in with valid username "username" and valid password "valid_password" and is on the inbox page
        And user navigates to the settings page
        When user adds a folder with name "Test Folder"
        Then a folder is successfully created
