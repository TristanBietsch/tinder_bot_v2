from selenium import  webdriver
from random import randint
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import username, password

LIKE_XPATH = '///*[@id="q-600306533"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[5]/div/div[4]/button'
DISLIKE_XPATH = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]'


class TinderBot():
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self):
        self.driver.get('https://tinder.com')
        
        sleep(3)
         
        self.driver.find_element_by_xpath('//*[@id="q-600306533"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')   
        
        sleep(2)
        
        login_btn = self.driver.find_element_by_xpath('//*[@id="q-600306533"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')   
        login_btn.click()
        
        sleep(2)
        
        fb_btn = self.driver.find_element_by_xpath('//*[@id="q1654454959"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()
        
        sleep(2)
        
        #switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        
        sleep(2)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        
        sleep(2)
        
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)
        
        #login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0_Z3"]')
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()
        
        sleep(2)
        
        self.driver.switch_to_window(base_window)
        
        sleep(2)
        
        popup_1 = self.driver.find_element_by_xpath('//*[@id="q1654454959"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        
        sleep(2)
        
        popup_2 = self.driver.find_element_by_xpath('//*[@id="q1654454959"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
        
        sleep(5)
        
    # XPATH Version
    # def like(self):
    #     like_btn = self.driver.find_element_by_xpath(LIKE_XPATH)
    #     like_btn.click()

    # XPATH VERSION
    # def dislike(self):
    #     dislike_btn = self.driver.find_element_by_xpath(DISLIKE_XPATH)
    #     dislike_btn.click()
    
    # Like Profile
    def like(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)

    # Dislike Profile
    def dislike(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_LEFT)

    def auto_swipe(self):
        while True:
            sleep(1)
            
            self.like()
            # auto-close popup
            # try:
            # except Exception:
            #     try:
            #         self.close_popup()
            #     except Exception:
            #         self.close_match()

    # def close_popup(self):
    #     popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
    #     popup_3.click()

    # def close_match(self):
    #     match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
    #     match_popup.click()

bot = TinderBot()
bot.login()