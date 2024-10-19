Feature: Saving txt files

Scenario: valid file name pattern
    Given there are txt files in the folder
    When the file has the file name pattern "<fileNameRegex>"
    Then add the prefix "r_" before the file name
    And add the sufix "unziped" plus datetime
    And move the file to "r_input_files" S3 bucked //this is the input bucket to the data ingesting app
    Examples:
    |fileNameRegex|
    |*IdNumber*.txt|
    |*subNumber*.txt|

Scenario: first txt file arrived
    Given the file came from a registed interface file
    When the file "<fileName>" is received
    And the table interfaces_input does not have a record with interface "<interface>", the "<originalDate>" plus the "<unzipedDate>"
    Then add a record to table interfaces_input with interface "<interface>", the "<originalDate>" plus the "<unzipedDate>"
    And save the file content to table "<fileId>"
    And update the colunm "<fileId>" on interfaces_input with the "<fileName>"
    And update the colunm status on interfaces_input with the INPROGRESS

    Examples:
    |fileName                                           |fileId     |interface      |originalDate   |unzipedDate    |      
    |r_BR03_20240205_IdNumber_unzip202402051015.txt     |IdNumber   |BR03           |20240205       |202402051015   |

Scenario: subsequent txt file arrived
    Given the file came from a registed interface file
    When the file "<fileName>" is received
    And the table interfaces_input has a record with interface "<interface>", the "<originalDate>" plus the "<unzipedDate>"
    Then save the file content to table "<fileId>"
    And update colunm "<fileId>" on interfaces_input with the "<fileName>"
    And update colunm status on interfaces_input with the INPROGRESS

    Examples:
    |fileName                                           |fileId     |interface      |originalDate   |unzipedDate    |        
    |r_BR03_20240205_IdNumber_unzip202402051015.txt     |IdNumber   |BR03           |20240205       |202402051015   |