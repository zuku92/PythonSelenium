
import unittest
from selenium import webdriver
from time import sleep


class AddToCardTestCase(unittest.TestCase):
    url = 'https://2nabiji.ge/ge/product/puri-tcvavis-mzethamze-tcvia'

    def test_add_to_shopping_card(self):

        browser = webdriver.Chrome(executable_path='/home/kali/PycharmProjects/selenium/chromedriver')
        browser.get(self.url)
        add_card = browser.find_element_by_xpath('//*[@id="commonButton"]')
        add_card.click()
       
        
        
	




