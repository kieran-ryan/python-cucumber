Feature: Login

    @login
    Scenario: Log in to Gmail
        Given user is on the login page
        When user enters valid username "username" and valid password "valid_password"
        Then the user is logged in
