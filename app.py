import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import datetime

def login(driver, username, password):
    user_block = driver.find_element(By.NAME, 'user[email]')
    pw_block = driver.find_element(By.NAME, 'user[password]')

    user_block.clear()
    pw_block.clear()

    user_block.send_keys(f'{username}')
    pw_block.send_keys(f'{password}')

    submit_button = driver.find_element(By.XPATH, "//input[@name='commit']")
    submit_button.click()

    book_now_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'BOOK NOW')))
    book_now_button.click()


    #sometimes a notification pops up, must hit accept to proceed
    try:
        accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='commit']")))
        if (accept_button):
            accept_button.click()
    except:
        print('no notification')

def book_time(driver, sport, time_slot, court, day):
    sport_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[text()='{sport}']")))
    sport_button.click()

    week_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='DaysRangeOptions']//button[{day}]")))
    week_button.click()

    driver.execute_script("window.scrollTo(0, 1000)")

    try:
        time_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[normalize-space()='{time_slot}']")))
        time_button.click()
    except:
        return 'error: time selected unavailable'

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    try:
        court_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[normalize-space()='{court}']")))
        court_button.click()
    except:
        return 'court selected unavailable'

    time.sleep(1)

    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='position_sticky_bottom_on_mobile bk_white mtb20 ptb10 z-index-1']//div[2]//button[1]")))
    next_button.click()

    time.sleep(1)

    users_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='1']")))
    users_button.click()

    next_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='position_sticky_bottom_on_mobile bk_white mtb20 ptb10 z-index-1']//div[1]//button[1]")))
    next_button2.click()


    book_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'large')]")))
    book_button.click()

    return ('successfully booked')

# correctly gets the box number each day will be represented in corresponding to the current day of the week
def weekday(day):
    current_date = datetime.datetime.today()
    current_day = current_date.weekday()

    match current_day:
        case 0:
            weekday_number = {
                "Monday": 7,
                "Tuesday": 1,
                "Wednesday": 2,
                "Thursday": 3, 
                "Friday": 4,
                "Saturday": 5,
                "Sunday": 6,
            }
            return weekday_number[day]
        case 1:
            weekday_number = {
                "Monday": 6,
                "Tuesday": 7,
                "Wednesday": 1,
                "Thursday": 2, 
                "Friday": 3,
                "Saturday": 4,
                "Sunday": 5,
            }
            return weekday_number[day]
        case 2:
            weekday_number = {
                "Monday": 5,
                "Tuesday": 6,
                "Wednesday": 7,
                "Thursday": 1, 
                "Friday": 2,
                "Saturday": 3,
                "Sunday": 4,
            }
            return weekday_number[day]
        case 3:
            weekday_number = {
                "Monday": 4,
                "Tuesday": 5,
                "Wednesday": 6,
                "Thursday": 7, 
                "Friday": 1,
                "Saturday": 2,
                "Sunday": 3,
            }
            return weekday_number[day]
        case 4:
            weekday_number = {
                "Monday": 3,
                "Tuesday": 4,
                "Wednesday": 5,
                "Thursday": 6, 
                "Friday": 7,
                "Saturday": 1,
                "Sunday": 2,
            }
            return weekday_number[day]
        case 5:
            weekday_number = {
                "Monday": 2,
                "Tuesday": 3,
                "Wednesday": 4,
                "Thursday": 5, 
                "Friday": 6,
                "Saturday": 7,
                "Sunday": 1,
            }
            return weekday_number[day]
        case 6:
            weekday_number = {
                "Monday": 1,
                "Tuesday": 2,
                "Wednesday": 3,
                "Thursday": 4, 
                "Friday": 5,
                "Saturday": 6,
                "Sunday": 7,
            }
            return weekday_number[day]


def main(username, password, sport, time, court, day):
    driver = webdriver.Chrome()
    login_url = 'https://pcmarc.playbypoint.com/users/sign_in'
    driver.get(login_url)

    if (sport == 'pickleball'):
        sport = 'Indoor Pickleball'
    else:
        sport = 'Indoor Tennis Courts'

    day_selected = weekday(day)

    try:
        login(driver, username, password)
    except:
        print('unsuccessful login')
 
    status = book_time(driver, sport, time, court, day_selected)
    print(status)



main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

# python3 app.py wbschmae@gmail.com iridepc22 pickleball 7:30-8am 'Pickleball 9B' Wednesday


