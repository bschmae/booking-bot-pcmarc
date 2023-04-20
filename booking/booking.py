from selenium import webdriver 
from selenium.webdriver.common.by import By
import os
import booking.constants as const
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"./chromdriver_mac64", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.maximize_window()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    #access the first page
    def land_first_page(self):
        self.get(const.LOGIN_URL) 

    #login
    def login(self, username, password):
        user_block = self .find_element(By.NAME, 'user[email]')
        pw_block = self.find_element(By.NAME, 'user[password]')

        user_block.clear()
        pw_block.clear()

        user_block.send_keys(f'{username}')
        pw_block.send_keys(f'{password}')

        submit_button = self.find_element(By.XPATH, "//input[@name='commit']")
        submit_button.click()
    
    #navigate to booking page
    def nav_to_booking_page(self):
        book_now_button = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'BOOK NOW')))
        book_now_button.click()

        try:
            accept_button = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='commit']")))
            if (accept_button):
                accept_button.click()
        except:
            print('no notification')
    
    #make reservation
    def make_res(self, sport, day, time_slot, court):
        if (sport == 'pickleball'):
            sport = 'Indoor Pickleball'
        else: 
            sport = 'Indoor Tennis Courts'

        #select sport
        sport_button = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[text()='{sport}']")))
        sport_button.click()

        #select day
        week_button = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='DaysRangeOptions']//button[{day}]")))
        week_button.click()

        self.execute_script("window.scrollTo(0, 1000)")

        #select time slot
        try:
            time_button = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[normalize-space()='{time_slot}']")))
            time_button.click()
        except:
            self.close()
            return 'error: time selected unavailable'


        #scroll down
        self.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        #select court
        try:
            court_button = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[normalize-space()='{court}']")))
            court_button.click()
        except:
            self.close()
            return 'court selected unavailable'

        time.sleep(1)

        #next form
        next_button = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='position_sticky_bottom_on_mobile bk_white mtb20 ptb10 z-index-1']//div[2]//button[1]")))
        next_button.click()

        time.sleep(1)

        #select number of users
        users_button = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='1']")))
        users_button.click()

        #next form
        next_button2 = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='position_sticky_bottom_on_mobile bk_white mtb20 ptb10 z-index-1']//div[1]//button[1]")))
        next_button2.click()

        #finalize the reservation
        book_button = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'large')]")))
        book_button.click()

        self.close()
        return ('successfully booked')
    
    def weekday(self, day):
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

