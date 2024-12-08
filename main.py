from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import json
from basic_functions import get_url, apply

# Get basic data
attachments_path = "./Attachments/"
# Load data from config.json
with open('config.json', 'r') as file:
    data = json.load(file)

# Open the browser
driver = webdriver.Edge()
driver.maximize_window()

# start with page 1
page = 1

while True:
    # GET TO PAGE
    url = get_url(page)
    driver.get(url)
    
    # ACCEPT COOKIES
    try:
        accept_cookies_button = driver.find_element(By.CLASS_NAME, 'cc-allow-right')
        accept_cookies_button.click()
        time.sleep(1)
    except:
        None
    
    
    # FIND JOBS
    jobs = driver.find_elements(By.CSS_SELECTOR, 'div[class="row g-20"] > div')
    if not jobs:
        break
    
    new_rows = []
    
    # FOR EACH JOB
    for job in jobs:
        # OPEN JOB IN NEW TAB
        ActionChains(driver)\
        .key_down(Keys.CONTROL)\
        .click(job)\
        .key_up(Keys.CONTROL)\
        .perform()
        
        # SWITCH TO TAB
        driver.switch_to.window(driver.window_handles[1])
        
        # APPLY TO THE JOB
        current_url = driver.current_url
        new_rows.append({"URL": current_url, "Page": page})
        apply(driver, data, attachments_path)
        
        # CLOSE TAB
        driver.close()
        # SWITCH TO ORIGINAL TAB
        driver.switch_to.window(driver.window_handles[0])
    
    # CHANGE PAGE
    page += 1


driver.quit()