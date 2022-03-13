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

trackBtns = driver.find_elements(By.LINK_TEXT, 'Track')
for btn in trackBtns:
    btn.click()
    driver.implicitly_wait(3)
    
    
    

# count = 0
# while count < len(trackBtns):
#     trackBtns[count].click()
#     driver.find_element(By.NAME, "email").clear()
#     driver.find_element(By.NAME, "email").send_keys("adewole@gmail.com")

#     driver.find_element(By.NAME, 'cell_name').clear()
#     driver.find_element(By.NAME, 'cell_name').send_keys(cell_name)

#     Select(driver.find_element(By.NAME, 'church_message')).select_by_value('4')

#     Select(driver.find_element(By.NAME, 'foundation_message')).select_by_value('7')

#     driver.find_element_by_xpath("//button[@type='submit']").click()

#     count += 1