import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver):
    user_block = driver.find_element(By.NAME, 'user[email]')
    pw_block = driver.find_element(By.NAME, 'user[password]')

    user_block.clear()
    pw_block.clear()

    user_block.send_keys('wbschmae@gmail.com')
    pw_block.send_keys('iridepc22')

    submit_button = driver.find_element(By.XPATH, "//input[@name='commit']")
    submit_button.click()

def book_time(driver):
    book_now_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'BOOK NOW')))
    book_now_button.click()


    #sometimes a notification pops up, must hit accept to precede
    try:
        accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='commit']")))
        if (accept_button):
            accept_button.click()
    except:
        print('no notification')

    sport_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Indoor Pickleball']")))
    sport_button.click()

    week_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='DaysRangeOptions']//button[4]")))
    week_button.click()

    time_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='7:30-8am']")))
    time_button.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    court_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Pickleball 9A']")))
    court_button.click()

    time.sleep(2)

    next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='position_sticky_bottom_on_mobile bk_white mtb20 ptb10 z-index-1']//div[2]//button[1]")))
    next_button.click()

    time.sleep(2)
    
    users_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='1']")))
    users_button.click()

    next_button2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='position_sticky_bottom_on_mobile bk_white mtb20 ptb10 z-index-1']//div[1]//button[1]")))
    next_button2.click()


    book_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'large')]")))
    book_button.click()

def main():
    driver = webdriver.Chrome()
    login_url = 'https://pcmarc.playbypoint.com/users/sign_in'
    driver.get(login_url)

    login(driver)

    book_time(driver)

main()


    