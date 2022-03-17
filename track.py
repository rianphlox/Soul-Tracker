#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
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
options.add_argument('disable-infobars')
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
tds = trs[sys.argv[1]].find_elements(By.TAG_NAME, 'td')
# print(len(tds), 'were found')
a = tds[len(tds) - 1].find_element(By.TAG_NAME, 'a')
a.click()

modal = driver.find_element(By.CLASS_NAME, 'modal')
modal_dialog = modal.find_element(By.CLASS_NAME, 'modal-dialog')
modal_content = modal_dialog.find_element(By.CLASS_NAME ,'modal-content')
print('modal-content was found')
modal_body = modal_content.find_element(By.CLASS_NAME, 'modal-body')
rows = driver.execute_script("return document.querySelectorAll('#ModalUpdate > div > div > div > div')")
# print(len(rows), 'rows were found')
col_md = rows[2].find_element(By.CLASS_NAME , 'col-md-6')
form_group = col_md.find_element(By.CLASS_NAME, 'form-group')
email_input = form_group.find_element(By.TAG_NAME ,'input')
email_input.clear()
email_input.send_keys(t_email)
print('Email input was found!\n\n\nFinally!!!\n')
try:
    col_md_cell = rows[3].find_element(By.CLASS_NAME, 'col-md-6')
    print('col_md_cell Was found!\n\n\n')
    try:
        form_group_cell = col_md_cell.find_element(By.CLASS_NAME, 'form-group')
        print("Form Group was found\n\n")
        try:
            cell_input = form_group_cell.find_element(By.TAG_NAME, 'input')
            print('cell input was found')
            cell_input.clear()
            cell_input.send_keys(choice(cell_name))
            # rows[4].find_element(By.CLASS_NAME, 'col-md-6').find_element(By.CLASS_NAME, 'form-group').find_element(By.TAG_NAME, 'select')
            try:
                # both_selects = rows[4].find_element(By.CLASS_NAME, 'col-md-6').find_element(By.CLASS_NAME, 'form-group').find_element(By.TAG_NAME, 'select') 
                # col_md_fs = rows[4].find_elements(By.CLASS_NAME, 'col-md-6')
                Select(rows[4].find_element(By.CLASS_NAME, 'col-md-6').find_element(By.CLASS_NAME, 'form-group').find_element(By.TAG_NAME, 'select')).select_by_value('4')

                print("found church service too")

                try:
                    col_md_fs = rows[4].find_elements(By.CLASS_NAME, 'col-md-6')
                    Select(col_md_fs[1].find_element(By.CLASS_NAME, 'form-group').find_element(By.TAG_NAME, 'select')).select_by_value('7')
                    print("Done: Found the Completed Foundation School Button\n\n")

                    try:
                        btns = rows[5].find_elements(By.TAG_NAME, 'button')
                        btns[1].click()
                    except NoSuchElementException as e:
                        print(f"{e}\n\n\n")
                except:
                    print('Ain\'t seen anything bruh\n\n\n')
            except:
                print("Error\n\n")

        except NoSuchElementException as e:
            print(f"{e}\nCellinput wasn't found\n")
    except NoSuchElementException as e:
        print(e)

except NoSuchElementException as e:
    print(e)
