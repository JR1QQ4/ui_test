*** Settings ***
Documentation     Simple example using SeleniumLibrary.Collections 用于使用集合相关的关键字
Library           SeleniumLibrary
Library    Collections
Resource    业务关键字.txt

*** Variables ***


*** Test Cases ***
Test1
    comment    1.打印
    log    Hello world

    comment    2.设置变量
    ${a}    set variable    100
    log    ${a}

    comment    3.获取系统时间
    ${time}    get time
    log    ${time}

    comment    4.睡眠时间，强制等待
    comment    sleep    3

    comment    5.字符串的拼接
    ${str}    catenate    oracle    mysql    sqlserver
    log    ${str}

    comment    6.创建列表
    ${list1}    create list    功能测试    自动化测试    性能测试
    log    ${list1}
    @{list2}    create list    功能测试    自动化测试    性能测试
    log many    @{list2}

    comment    7.创建字典
    ${dic}    create dictionary    name=百里    age=18
    log    ${dic}
    log    ${dic}[name]
    ${keys}    get dictionary keys    ${dic}
    log    ${keys}
    ${values}    get dictionary values    ${dic}
    log    ${values}
    ${key_value}    get from dictionary    ${dic}    name
    log    ${key_value}

    comment    8.执行Python里面的方法
    ${random_number}    evaluate    random.randint(1, 101)    modules=random
    log    ${random_number}
    ${times}    evaluate    time.time    modules=time
    log    ${times}

    comment    9.执行Python自定义的方法
    import library    ${CURDIR}/test.py
    ${a}    evaluate    int(10)
    ${b}    evaluate    int(20)
    ${return_result}    add    ${a}    ${b}
    log    ${return_result}

    comment    10.流程控制IF
    ${age}    set variable    22
    run keyword if    ${age}>30    log    年龄太大
    ...    else if    18<=${age}<=30    log    正好
    ...    else    log    未成年

    comment    11.流程控制FOR
    FOR    ${a}    IN    功能测试    自动化测试    性能测试
    log    ${a}
    END
    ${list3}    create list    功能测试    自动化测试    性能测试
    FOR    ${a}    IN    ${list3}
    log    ${a}
    END
    FOR    ${a}    IN RANGE    1    11
    run keyword if    ${a}==5    exit for loop
    log    ${a}
    END

Test2
    百度搜索    robotframework    robotframework

*** Keywords ***



