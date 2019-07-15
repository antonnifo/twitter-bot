import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class TwitterBot():
    
    def __init__(self,username,password):
        
        self.username = username
        self.password = password
        options = Options()
        options.headless = True
        firefoxPath="/usr/local/bin/geckodriver"
        self.bot = webdriver.Firefox(options=options,executable_path=firefoxPath)

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/")
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        p_word= bot.find_element_by_name('session[password]')
        email.clear()
        p_word.clear()
        email.send_keys(self.username)
        p_word.send_keys(self.password)
        p_word.send_keys(Keys.RETURN)
        time.sleep(3)
