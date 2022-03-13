#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyautogui as pg
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from random import choice, sample
from config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def handleReload(): 
    pg.click(753, 600)
    pg.press('right', 5)

def track():
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys("adewole@gmail.com")

    driver.find_element(By.NAME, 'cell_name').clear()
    driver.find_element(By.NAME, 'cell_name').send_keys(cell_name)

    Select(driver.find_element(By.NAME, 'church_message')).select_by_value('4')

    Select(driver.find_element(By.NAME, 'foundation_message')).select_by_value('7')

    driver.find_element_by_xpath("//button[@type='submit']").click()
    sleep(3)
    handleReload()


options = Options()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

driver.get(url)

driver.find_element(By.XPATH, '//*[@id="loginUsername"]').clear()
driver.find_element(By.XPATH, '//*[@id="loginUsername"]').send_keys(account)

driver.find_element(By.XPATH, '//*[@id="loginPassword"]').clear()
driver.find_element(By.XPATH, '//*[@id="loginPassword"]').send_keys(password)

driver.find_element(By.XPATH, '//*[@id="sign-in-form"]').submit()
sleep(1)

driver.get(t_url)
sleep(2)

handleReload()

# len_of_list = len(driver.find_elements(By.LINK_TEXT, 'Track'))
# xpaths = "xpath=//table[@id='mytable']/tbody/tr[{count}]/td[7]/a"
# for count, btn in enumerate(trackBtns, start=1):
#     btn.click()
#     driver.implicitly_wait(3)
#     track()
tbody = driver.execute_script("return document.querySelector('tbody')")
# print(f"{tbody} was returned")
trs = tbody.find_elements(By.TAG_NAME, 'tr')
# trs[0].find
# print(len(trs), 'was found')
tds = trs[0].find_elements(By.TAG_NAME, 'td')
# print(len(tds), 'were found')
a = tds[len(tds) - 1].find_element(By.TAG_NAME, 'a')
a.click()
try:
    modal = driver.find_element(By.CLASS_NAME, 'modal')
    try:
        modal_dialog = modal.find_element(By.CLASS_NAME, 'modal-dialog')
        try:
            modal_content = modal_dialog.find_element(By.CLASS_NAME ,'modal-content')
            print('modal-content was found')
            try:
                modal_body = modal_content.find_element(By.CLASS_NAME, 'modal-body')
                try:
                    rows = modal_body.find_elements(By.TAG_NAME, "div")
                    print(len(rows), 'rows were found')
                    # print(rows[0])
                    # print(rows[0].text)
                except:
                    print('No such element as row')
            except:
                print('Modal Body not found')
        except:
            print("Modal Content not found")
    except NoSuchElementException:
        print("Modal Dialog not found")
except NoSuchElementException:
    print('No such element found')
