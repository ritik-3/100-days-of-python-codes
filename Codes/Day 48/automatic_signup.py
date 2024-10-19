from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
first_name.send_keys("Hello ji", Keys.TAB, "wahh ji wahh", Keys.TAB,"menahibatauga@jonnybhai.com", Keys.ENTER)




