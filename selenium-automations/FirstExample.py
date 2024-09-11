# Step 1. Import the Necessary Classes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Step 2. Create a WebDriver Instance
######################################
# Using chrome - option 1
######################################
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# ######################################
# # Using chrome - option 2
# ######################################
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # noqa

# ######################################
# # Using Edge
# ######################################
# edge_driver = "Drivers/edge/msedgedriver.exe"
# options = webdriver.EdgeOptions()
# options.add_argument('--headless')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# options.add_argument("log-level=3")  # INFO 0, WARNING 1, LOG_ERROR 2, LOG_FATAL 3  # noqa
# service = webdriver.EdgeService(executable_path=edge_driver)
# driver = webdriver.Edge(service=service, options=options)

# ######################################
# # Using Firefox
# ######################################
# options = webdriver.FirefoxOptions()
# options.add_argument('--headless')
# service = webdriver.FirefoxService()
# driver = webdriver.Firefox(service=service, options=options)

# Step 3. Load a Website
driver.get("https://www.python.org")

# Step 4. Check the Page Title
print(driver.title)  # It should be `Welcome to Python.org`

# Step 5. Interact with the Search Bar
search_bar = driver.find_element(by=By.NAME, value="q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

# Step 6. Verify the Resulting URL
print(driver.current_url)
# It should be: https://www.python.org/search/?q=getting+started+with+python&submit=  # noqa

# Step 7. Open a new tab with a different URL
driver.execute_script("window.open('https://www.google.com', '_blank');")

# Step 8. Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)

# Step 9. Perform actions in the new tab (e.g., search for 'Selenium')
search_bar = driver.find_element(by=By.NAME, value="q")
search_bar.clear()
search_bar.send_keys("Selenium")
search_bar.send_keys(Keys.RETURN)

# Step 10. Close current tab
driver.close()

# Step 11. Switch back to the original tab
driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)

# Step 12. Close the Browser
driver.close()
