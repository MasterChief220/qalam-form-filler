from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Here
driver = webdriver.Chrome(options=options)
driver.get("https://qalam.nust.edu.pk/")

title = driver.title 
driver.implicitly_wait(3)  
#text_box = driver.find_element(by=By.NAME, value="login") 
isvisible = driver.find_element(By.NAME, "login").is_displayed() 
print(isvisible) 
text_box = driver.find_element(by=By.NAME, value="login")
text_box.send_keys("mbassam.mts42ceme") 
text_box = driver.find_element(by=By.NAME, value="password")
text_box.send_keys("BK@nust#123") 
login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-nust.btn-block.py-3.mt-4")  # Adjust the CSS selector to match the HTML attribute of the login button 
login_button.click()
print(driver.current_url) 

wait = WebDriverWait(driver, 10)
driver.find_element(By.PARTIAL_LINK_TEXT, "color_input").click()
  