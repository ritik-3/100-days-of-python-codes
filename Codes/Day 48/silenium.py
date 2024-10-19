from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

date_py= driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

for time in date_py:
    print(time.text)

driver.quit()