*** Settings ***
Library    SeleniumLibrary
Test Setup    Open Url
Test Teardown    Close Browser


*** Variables ***
${BROWSER}    Chrome
${URL}    https://opensource-demo.orangehrmlive.com/
${USER}    Admin
${PASSWORD}    admin123


*** Test Cases ***
Login Page
    [Documentation]    Test for login action
    [Tags]    Login
    When I Login With Correct User And Pwd
    Then Access Should Be Provided 
    Capture Page Screenshot    Login.png


Logout From Site
    [Documentation]    Test for logout action
    [Tags]    Logout
    When I Login With Correct User And Pwd
    And I Logout
    Then Session Should Be Closed
    Capture Page Screenshot    Logout.png
    

*** Keywords ***
Open Url
    # Headless mode
    ${options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --headless
    Open Browser    ${URL}    ${BROWSER}    options=${options}
    # # Browser visible
    # Create WebDriver        ${BROWSER}
    # Maximize Browser Window
    # Go To    ${URL}
    Wait For Condition    return !!document.body


I Login With Correct User And Pwd
    Wait Until Element Is Visible    name:username
    Input Text    //input[@name="username"]    ${USER}
    Input Password    name:password     ${PASSWORD}
    Click Button    xpath=//button[@type='submit']

Access Should Be Provided
    Wait Until Element Is Visible    xpath=//h6[text()='Dashboard']
    Title Should Be    OrangeHRM    


I Logout
    Wait Until Element Is Visible    xpath=//img[@alt='profile picture']
    Click Element    xpath=//img[@alt='profile picture']
    Click Element    xpath=//a[text()='Logout']
    

Session Should Be Closed
    Wait For Condition    return document.readyState == "complete"
    Location Should Be    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
    

