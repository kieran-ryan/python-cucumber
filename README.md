# python-cucumber

## Setup:

#### Clone the repo

`$ git clone git@github.com:tbeede/python-cucumber.git`

`$ cd python-cucumber`

#### Configure the project

Navigate to

`$ cd features/environment.py`

Add your Gmail username and password credentials.

#### To run all tests
`$ behave`

#### To run an individual test by feature tag

`$ behave --tags=tag_name`

For example, 

`$ behave --tags=login`

#### Features and Test Steps in This Repo

`before_each` is configured on all tests to log in by default, therefore the login feature tests will have to be run separately for now or they will interfere with the other tests.

Also, a LOT of custom xpath had to be written to handle the dynamic elements, and for this reason some tests are stronger and more reliable than others. The final test in the list below is very finicky when handling the "move to" dropdown to move a message into a folder.

* Login to gmail
* Cannot login with invalid password
* Compose and send an email*
* Filter/search the email list*
* Delete an email
* Add a folder
* Move a message into the folder*

*Requires message parameters to be set in `feature` file


### About the Behave Framework

Behave is a Gherkin-based Behavior-Driven Development (BDD) tool developed especially for Python. Read more about it [here](https://behave.readthedocs.io/en/latest/).



