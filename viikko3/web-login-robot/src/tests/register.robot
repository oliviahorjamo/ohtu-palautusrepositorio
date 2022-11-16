*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Correct Credentials
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  k
    Set Password Confirmation  k
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle1234
    Submit Credentials
    Register Should Fail With Message  Passwords dont match

Login After Successful Registration
    Set Username  olivia
    Set Password  olivia123
    Set Password Confirmation  olivia123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  olivia
    Set Password  olivia123
    Submit Login Credentials
    Login Should Succeed


Login After Failed Registration
    Set Username  kalle
    Set Password  k
    Set Password Confirmation  k
    Submit Credentials
    Register Should Fail With Message  Password too short
    Go To Login Page
    Set Username  kalle
    Set Password  k
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password



*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Login Credentials
    Click Button  Login


Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

#Create User And Go To Login Page
 #   Create User  kalle  kalle123
  #  Go To Login Page
   # Login Page Should Be Open

