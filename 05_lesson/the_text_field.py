from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
Search = driver.find_element(By.CSS_SELECTOR, "#APjFqb")
Search.send_keys("Selenium")
Search.send_keys(Keys.RETURN)
print(Search)
driver.quit()