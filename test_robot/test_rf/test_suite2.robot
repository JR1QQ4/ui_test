*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***


*** Test Cases ***
Case1
    open browser    http://www.baidu.com    chrome
    comment    隐式等待
    set browser implicit wait    5
    sleep    2
    maximize browser window
    sleep    2
    set window size    1024    768
    sleep    2
    ${width}    ${height}    get window size
    sleep    2
    go back
    sleep    2
    go to    http://www.baidu.com
    sleep    2
    reload page
    sleep    2
    ${title}    get title
    log    ${title}
    sleep    2
    close browser


*** Keywords ***

