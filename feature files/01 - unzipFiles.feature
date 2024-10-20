Feature: Extracting multiple files from a zip files

@Done
Scenario: valid interface
    Given we received a new zip file in the s3 bucket "r_input"
    When the file name matches the accepted interfaces in the interfaces.txt on the S3 bucket "r_config_interface"
    Then the the file is unziped
    And the zip file is moved to "r_input_archive"

Scenario: not registered interface
    Given we received a new zip file in the s3 bucket "r_input"
    When the file name does not matches the accepted interfaces in the interfaces.txt on the S3 bucket "r_config_interface"
    Then a error(not registered) file is send to the data ingesting app input folder
    And the zip file is moved to "r_input_error"

Scenario: the data ingesting app receives an error file
    Given a error file is receive by the data ingesting app
    When the file has info about the zip file
    Then an email describing the issue at the zip file is send to the customer
    And the zip file is moved to "r_input_error"

Scenario: expected number of txt files
    Given we received a new zip file in the s3 bucket "r_input"
    When the file is unziped
    Then there are 7 txt files

Scenario: unziped file without all txt files
    Given we received a new zip file in the s3 bucket "r_input"
    When the file is unziped
    And not all expected files are present
    Then a error(missing files) file is send to the data ingesting app input folder
    And the txt files are deleted
    And the zip file is moved to "r_input_error"
