*** Settings ***
Library    Browser
Suite Setup    New Browser    browser=${BROWSER}    headless=${HEADLESS}
Test Setup    New Context    viewport={'width': 800, 'height': 400}
Test Teardown    Close Context
Suite Teardown    Close Browser


*** Variables ***
${BROWSER}    chromium
${HEADLESS}    True
${URL}    https://opensource-demo.orangehrmlive.com/
${USER}    Admin
${PASSWORD}    admin123
${SLEEP}    0s

*** Test Cases ***
Login Page
    [Documentation]    Test for login action
    [Tags]    Login
    Given Site Is Open
    When I Login With Correct User And Pwd
    Then Access Should Be Provided
    Take Screenshot    login
    Sleep    ${SLEEP}


Logout from Site
    [Documentation]    Test for logout action
    [Tags]    Logout
    Given Site Is Open
    When I Login With Correct User And Pwd
    And I Logout
    Then Session Should Be Closed
    Take Screenshot
    Sleep    ${SLEEP}


*** Keywords ***
Site Is Open
    New Page    ${URL}
    

I Login With Correct User And Pwd
    Wait For Load State    state=load
    Fill Text    input[name="username"]     ${USER}
    Fill Text    input[name="password"]     ${PASSWORD}
    Click    button.orangehrm-login-button
    

Access Should Be Provided
    Get Title    ==    OrangeHRM


I Logout
    Wait For Load State    state=load
    Click    i.oxd-userdropdown-icon  # Profile menu
    Click    a:text("Logout")  # Logout option


Session Should Be Closed
    Wait For Load State    state=load
    Get Url    ==    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
