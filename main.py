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
text_box.send_keys("mbassam.mts42ceme") # Enter your login id
text_box = driver.find_element(by=By.NAME, value="password")
text_box.send_keys("BK@nust#123") # Enter your password
login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-nust.btn-block.py-3.mt-4")  # Adjust the CSS selector to match the HTML attribute of the login button 
login_button.click()
print(driver.current_url) 

wait = WebDriverWait(driver, 10)
#driver.find_element(By.PARTIAL_LINK_TEXT, "student/evaluation/form").click()
tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "/student/evaluation/form")][2]')))
tab.click()
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)



num_questions = 8
for question_num in range(0, num_questions + 1):
    radio_input_name = f"134133_616922_439638{3 + question_num}"

    # Use JavaScript to click on the "Good" option directly
    script = f'''
        var radio = document.querySelector('input[name="{radio_input_name}"][value="4396380"]');
        if (radio) {{
            radio.click();
            console.log("Question {question_num}, Option 3 (Good) selected.");
        }} else {{
            console.error("Error selecting Question {question_num}, Option 3 (Good): Radio input not found.");
        }}
    '''
    driver.execute_script(script)

    # Pause for a moment to allow the change to be visually observed
    time.sleep(1)