from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
import logging as log
import sys


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)

#Registration Page 
def initialization():
    userInfo = json.load(open("login.json"))
    driver.get("https://login.bc.edu/nidp/idff/sso?id=19&sid=0&option=credential&sid=0&target=https%3A%2F%2Fservices.bc.edu%2Fcommoncore%2Fmyservices.do")
    ag_username = driver.find_element(By.ID, 'username')
    ag_username.send_keys(userInfo.get("user"))
    ag_password = driver.find_element(By.ID, 'password')
    ag_password.send_keys(userInfo.get("password"))
    ag_sign_in_button = driver.find_element(By.XPATH, '//*[@id="fm1"]/button')
    ag_sign_in_button.click()
    driver.implicitly_wait(10)
    driver.get("https://eaen.bc.edu/student-registration/#/")
    driver.implicitly_wait(30)
    term_pullup = driver.find_element(By.XPATH, '//*[@id="fddAtpSelectorInputTopDiv"]/div/div/div/span/i')
    term_pullup.click()
    selectSem = makeSelection(['//*[@id="ui-select-choices-row-0-', '"]'], userInfo.get("semester"), 3)
    selectSem.click()
    selectPlan = makeSelection(['//*[@id="tabularCCRegistrationRequestItemSelectorRegistrationPlan','"]'], userInfo.get("plan"), 3)
    selectPlan.click()


def makeSelection(path, selection, length):
    for i in range(length):
        potential = driver.find_element(By.XPATH, path[0]+str(i)+path[1]) #Have it save the first half of string in path 0 and second in path 1
        innerString = potential.get_attribute('innerHTML')
        log.info(innerString) 
        if selection in innerString:
            return potential
    return

def refresh():
    driver.implicitly_wait(60)
    dropper = driver.find_element(By.XPATH, '//*[@id="contextUserName"]/i')
    dropper.click()
    driver.implicitly_wait(30)
    refresher = driver.find_element(By.XPATH, '//*[@id="refreshSessionBtn"]')
    refresher.click()
    driver.implicitly_wait(45)

def enroll():
    first = '//*[@id="tabularCCRegistrationRequestItemSelectorCheckbox'
    for i in range(15):
        time.sleep(3)
        driver.implicitly_wait(5)
        id = first + str(i) + '"]'
        try:
            checkbox = driver.find_element(By.XPATH, id)
            checkbox.click()
            enroll = driver.find_element(By.XPATH, '//*[@id="register-button"]')
            enroll.click()
        except:
            break
#Main
def main():
    error = initialization()
    driver.implicitly_wait(5)
    time.sleep(5)
    while True:
         enroll()
         refresh()
         time.sleep(300)

main()


