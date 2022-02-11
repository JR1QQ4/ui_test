*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***


*** Test Cases ***
LocatorTest
    open browser    http://www.baidu.com    chrome
    set browser implicit wait    5
#    input text    id=kw    id定位
#    input text    name=wd    name定位
#    input text    identifier=wd    可以是id可以是name
#    click element    link=新闻    # 链接文本点击元素
#    click element    partial link=新    # 点击链接，包含
#    input text    xpath=//form/span/input    xpath相对路径定位
#    input text    xpath=//input[@autocomplete="off" and @class="s_ipt"]    xpath属性定位
#    input text    xpath=//input[contains(@autocomplete, "of")]    xpath部分属性定位
#    click element    xpath=//a[text()="新闻"]    # xpath文本定位
#    input text    css=input[autocomplete="off"][class="s_ipt"]    css属性定位
#    input text    css=input[autocomplete^="of"]    css部分属性定位
    click element    css=div#s-top-left a:nth-child(3)    # css子元素定位

    sleep    2
    close browser

*** Keywords ***

