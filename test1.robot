*** Settings ***
Library  Selenium2Library

*** Variables ***
${HOMEPAGE} http://www.google.fi
${BROWSER}  chrome
*** Test Cases ***
Google devops and find eficode

*** Keywords ***
Google and check results
    [Arguments] ${searchkey} ${result}


Go to homepage
    Open Browser ${HOMEPAGE} ${BROWSER}