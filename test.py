from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Here
driver = webdriver.Chrome(options=options)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title 
driver.implicitly_wait(0.5)
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button") 
text = driver.find_element(By.NAME, "mytext").text 
