from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
ser = Service("C:/seleniumDrivers/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get('https://www.linkedin.com')
time.sleep(2)

'''log in infos'''
try:
    username = driver.find_element(By.ID,"session_key")
    password = driver.find_element(By.ID,"session_password")

    username.send_keys('mail address goes here')
    password.send_keys('password goes here')
    time.sleep(2)

    submit = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
    submit.click()
    print(f"{'-'*6} Logged in succesfully{'-'*6}")
except:
    print(f"{'-'*6}locators not found!{'-'*6}")

'''connecting'''
page = 1
while page <=4:
    url = f"https://www.linkedin.com/search/results/people/?origin=CLUSTER_EXPANSION&page={page}"
    driver.get(url)
    time.sleep(2)

    all_buttons = driver.find_elements(By.CLASS_NAME, "artdeco-button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)
        try:
            send = driver.find_element(By.ID,"ember98")
            driver.execute_script("arguments[0].click();", send)
        except:
            print("\n")
        time.sleep(4)
        try:
            close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
            driver.execute_script("arguments[0].click();", close)
        except:
            print("\n")
        time.sleep(2)
    print(f"{'-'*6}page = {page}{'-'*6} ")
    page +=  1
print(f"{'-'*6}script ended{'-'*6}")
driver.quit()