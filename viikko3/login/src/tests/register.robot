*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  matti
    Set Password  matti123
    Set Password Confirmation  matti123
    Click  button >> text=Register
    Get Title  !=  Register

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  matti123
    Set Password Confirmation  matti123
    Click  button >> text=Register
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  matti
    Set Password  m123
    Set Password Confirmation  m123
    Click  button >> text=Register
    Register Should Fail With Message  Password is too short

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Fail With Message  Username is already in use

*** Keywords ***
Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
