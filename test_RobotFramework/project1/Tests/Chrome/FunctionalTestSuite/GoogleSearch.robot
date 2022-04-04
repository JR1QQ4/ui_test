*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***


*** Test Cases ***
This is sample test case
    [Documentation]    Google test
    [Tags]    regression

    open browser    http://www.google.com    chrome
    close browser

*** Keywords ***

