# Importing required libraries

# npm install selenium

from selenium import webdriver
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Open Wikipedia website
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# Introduce a delay to ensure the page loads
time.sleep(2)

# Find and click on the 'Talk Page' link
talkPage_link = driver.find_element("id", "ca-talk")
talkPage_link.click()
time.sleep(2)

# Verify that we are on the 'Talk page' page
assert "Talk:Main Page" in driver.title

# Click on the 'View history' tab
view_history_tab = driver.find_element("id", "ca-history")
view_history_tab.click()
time.sleep(2)

# Find and Click on the 'View source' tab
view_source_tab = driver.find_element("id", "ca-viewsource")
view_source_tab.click()
time.sleep(2)

# Verify that we are on the 'View source page' page
assert "View source" in driver.title

# Find and click on the 'Main Page' link
mainPage_link = driver.find_element("id", "ca-nstab-main")
mainPage_link.click()
time.sleep(2)

# Find and click on the 'Create account' button
create_account_button = driver.find_element("id", "pt-createaccount-2")
create_account_button.click()
time.sleep(2)

# Verify that we are on the Create account page
assert "CreateAccount" in driver.current_url

print("Test passed successfully!")

# Close the browser
driver.quit()