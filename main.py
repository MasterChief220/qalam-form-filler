import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Here
driver = webdriver.Chrome(options=options)
driver.get("https://qalam.nust.edu.pk/")

title = driver.title 
driver.implicitly_wait(3)  

text_box = driver.find_element(by=By.NAME, value="login")
text_box.send_keys("") # Enter your login id
text_box = driver.find_element(by=By.NAME, value="password")
text_box.send_keys("") # Enter your password
login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-nust.btn-block.py-3.mt-4")  # Adjust the CSS selector to match the HTML attribute of the login button 
login_button.click()
print(driver.current_url) 

wait = WebDriverWait(driver, 10)
# Click on the first form link
second_form_link = driver.execute_script('return document.querySelectorAll(\'a[href*="/student/evaluation/form"]\')[2];')

# Click on the second form link
second_form_link.click()
driver.switch_to.window(driver.window_handles[1])

input("enter to exit")
