import pandas as pd
from selenium import webdriver
# from selenium.webdriver.common.keys import keys
from time import sleep, strftime
# import SMS
from random import randint # sleep random intervals
import SMS

# create class variable
class GPUBot(object):

    """
    Create selenium class to navigate to gamestop.com. From there, should the
    availability of the 3080 GPU change, the bot will send a message to the desired
    recepient
    """

    def __init__(self):
        url = 'https://www.gamestop.com/video-games/pc/components/graphics-cards/products/geforce-rtx-3080-10-gb-gddr6x-strix-graphic-card/11112926.html?condition=New'

        # launch chrome browser
        self.driver = webdriver.Chrome(r'C:\bin\chromedriver.exe')
        self.driver.get(url)
        sleep(randint(2, 10)) # sleep randim interval

    def get_availability(self):
        available = self.driver.find_element_by_xpath('//*[@id="primary-details"]/div[4]/div[13]/div[3]/div/div[1]/button').get_attribute('innerHTML')

        if available != 'Not Available':
            SMS.sendMessage()
        else:
            sleep(randint(2, 120)) # sleep
            self.driver.refresh()
            self.get_availability()

# run bot
GPUBot().get_availability()
