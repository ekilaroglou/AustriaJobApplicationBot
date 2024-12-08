from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import json
import os

def get_url(page):
    # Load data from config.json
    with open('config.json', 'r') as file:
        data = json.load(file)
        url = data["url"]
    url += f'&page={page}'
    return url

def apply(driver, data, attachments_path):
    # SALUTATION
    salutation = Select(driver.find_element(By.ID, "salutation"))
    if data["salutation"].lower().strip() == "mrs":
        salutation_index = 1
    elif data["salutation"].lower().strip() == "mr":
        salutation_index = 2
    else:
        # index = 3 means "other"
        salutation_index = 3
    salutation.select_by_index(salutation_index)

    # FIRSTNAME
    firstname_input = driver.find_element(By.ID, "firstname")
    firstname_input.send_keys(data["first_name"])

    # LASTNAME
    lastname_input = driver.find_element(By.ID, "lastname")
    lastname_input.send_keys(data["last_name"])

    # DATE
    hidden_input = driver.find_element(By.NAME, 'birthday')
    # Change the value using JavaScript
    new_value = f'{data["date_of_birth"]}T00:00:00'
    driver.execute_script("arguments[0].value = arguments[1];", hidden_input, new_value)

    # PHONE
    phone_input = driver.find_element(By.ID, "phone")
    phone_input.send_keys(data["phone"])

    # EMAIL
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(data["email"])

    # STREET
    street_input = driver.find_element(By.ID, "street")
    street_input.send_keys(data["street"])

    # NUMBER
    number_input = driver.find_element(By.ID, "number")
    number_input.send_keys(data["street_number"])

    # ZIP
    zip_input = driver.find_element(By.ID, "zip")
    zip_input.send_keys(data["zip"])

    # CITY
    city_input = driver.find_element(By.ID, "city")
    city_input.send_keys(data["city"])

    # COUNTRY
    country_input = driver.find_element(By.ID, "country")
    country_input.send_keys(data["country"])

    # MESSAGE
    message_input = driver.find_element(By.ID, "message")
    message_input.send_keys(data["cover_letter"])


    # UPLOAD FILES
    # Get a list of all files in the document directory
    documents = os.listdir(attachments_path)
    # If we have attachments
    if documents:
        # Get the absolute path of each document
        document_paths = [os.path.abspath(os.path.join(attachments_path, file)) for file in documents]
        files = "\n".join(document_paths)
    
        # PUT THE FILES IN files[]
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"][id="files[]"]')
        file_input.send_keys(f"{files}")
    
        # Wait for a while to ensure files are uploaded
        time.sleep(2)

    # CHECKBOX
    checkbox = driver.find_element(By.ID, "dsgvo")
    driver.execute_script("arguments[0].click();", checkbox)
    time.sleep(1)

    # SUBMIT
    # submit_button = driver.find_element(By.XPATH, "//button[normalize-space(text())='Send application']")
    # driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(200)