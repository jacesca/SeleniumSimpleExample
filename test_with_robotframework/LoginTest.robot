*** Settings ***
Library    Browser
Suite Setup    Login Site
Suite Teardown    Logout Site


*** Variables ***
${BROWSER}    chromium
${HEADLESS}    True
${URL}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${USER}    Admin
${PASSWORD}    admin123
${SLEEP}    0s

*** Test Cases ***
Succeed Login
    [Documentation]    Testing Login Page
    [Tags]    Login
    Access Should Be Provided


*** Keywords ***
Login Site
    New Browser
    New Context    viewport={'width': 1920, 'height': 1080}
    New Page    ${URL}
    Wait For Load State    state=load
    Fill Text    input[name="username"]     ${USER}
    Fill Text    input[name="password"]     ${PASSWORD}
    Click    button.orangehrm-login-button
    Wait For Load State    state=load
    

Logout Site
    Wait For Load State    state=load
    Click    i.oxd-userdropdown-icon  # Profile menu
    Click    a:text("Logout")  # Logout option
    Wait For Load State    state=load
    Get Url    ==    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
    Close Context
    Close Browser


Access Should Be Provided
    Wait For Load State    state=load
    Get Title    ==    OrangeHRM
