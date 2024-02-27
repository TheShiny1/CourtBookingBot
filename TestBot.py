from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time

email = 
password = 

url = "https://app.playbypoint.com/users/sign_in"
path = "venv/drivers/chromedriver.exe"

def run_at_specific_time():
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    wait = WebDriverWait(driver, 10)


    email_field = wait.until(EC.presence_of_element_located((By.ID, "user_email")))
    email_field.send_keys(email)

    password_field = driver.find_element(By.ID, "user_password")
    password_field.send_keys(password)


    login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[4]/input")
    login_button.click()

    while True:
        try:
            facility_link = driver.find_element(By.XPATH, "//*[@id=\"facility_home_box\"]/div[1]/div[2]/a")
            facility_link.click()
            break
        except:
            pass

    while True:
        try:
            date_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[1]/div/div/div/button[8]")
            date_button.click()
            break
        except:
            pass

    time.sleep(1)    
            
    while True:
        try:
            time_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[4]/div[2]/button[12]")
            time_button.click()
            break
        except:
            try:
                waitlist_modal = driver.find_element(By.XPATH, '//*[@id="waitlist_modal"]')
                close_button = driver.find_element(By.XPATH, '//*[@id="waitlist_modal"]/i')
                close_button.click()
            except:
                pass

    while True:
        try:
            court_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[5]/div/div/button[7]")
            court_button.click()
            break
        except:
            pass

    while True:
        try:
            confirm_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[2]/div[2]/button")
            confirm_button.click()
            break
        except:
            pass

    while True:
        try:
            player_selection = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/div/button")
            player_selection.click()
            break
        except:
            pass

    while True:
        try:
            book_confirm = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/div[4]/div/div/div/button")
            book_confirm.click()
            break
        except:
            pass
    pass


schedule.every().day.at("07:10").do(run_at_specific_time)

while True:
    schedule.run_pending()
    time.sleep(1)

driver.quit()
