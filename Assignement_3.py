from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open Kijiji.ca
driver.get("https://www.kijiji.ca/")

# Test 1: Search for a product
search_box = driver.find_element(By.ID, "SearchKeyword")
search_box.send_keys("car")
search_box.submit()

# Test 2: Click on a search result
search_result = driver.find_element(By.CSS_SELECTOR, "div.search-item")
search_result.click()
driver.implicitly_wait(20)


# Test 3: Check if the contact seller button is present
contact_seller_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div/header/div[3]/div/div[3]/div/div/div/a[2]")
if contact_seller_button.is_displayed():
    print("Sign in button is present")
else:
    print("Sign in button is not present")

# Test 4: Check if the Post Add button is present
post_add = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div/header/div[3]/div/div[3]/div/a[2]")
if post_add.is_displayed():
    print("Post add button is present")
else:
    print("Post add button is not present")

# Close the browser
driver.quit()
