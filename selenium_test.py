from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org/downloads/")
assert "Python" in driver.title
elem = driver.find_element(By.CLASS_NAME, "download-buttons")
elem = driver.find_element(By.PARTIAL_LINK_TEXT)
assert "No results found." not in driver.page_source
driver.close()