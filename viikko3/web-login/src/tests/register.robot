*** Settings ***
Resource            resource.robot
Resource            login.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset Application Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username    uusi
    Set Password    uusiuusi123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username    uu
    Set Password    kalle123
    Submit Credentials
    Register Should Fail With Message    Username too short

Register With Valid Username And Too Short Password
    Set Username    kalle
    Set Password    kall
    Submit Credentials
    Register Should Fail With Message    Password too short

Register With Valid Username And Invalid Password
    Set Username    kalle
    Set Password    kallekalle
    Submit Credentials
    Register Should Fail With Message    Password must contain numbers

Register With Nonmatching Password And Password Confirmation
    Input Text    username    uusi
    Input Text    password    kokeiluyksi0
    Input Text    password_confirmation    kokeilukaksi0
    Submit Credentials
    Register Should Fail With Message    Passwords don't match

Register With Username That Is Already In Use
    Set Username    testi
    Set Password    testitesti123
    Submit Credentials
    Register Should Fail With Message    User with username testi already exists

Login After Successful Registration
    Set Username    testaus
    Set Password    testaus12
    Submit Credentials
    Click Link    ohtu
    Click Button    Logout
    Input Text    username    testaus
    Input Password    password    testaus12
    Click Button    Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username    kalle
    Set Password    kallekalle
    Submit Credentials
    Click Link    Login
    Input Text    username    kalle
    Input Password    password    kallekalle
    Click Button    Login
    Login Page Should Be Open


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User    testi    testitesti123
    Go To Register page

Register Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Submit Credentials
    Click Button    Register

Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}
    Input Password    password_confirmation    ${password}
