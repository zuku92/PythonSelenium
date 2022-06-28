import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

class DeleteCardTestCase(unittest.TestCase):

    def setUp(self) -> None:

        self.browser = webdriver.Chrome(executable_path='/home/kali/PycharmProjects/pythonselenium/chromedriver')

    def test_delete(self):

        browser = self.browser
        browser.get('https://gorgia.ge/ka/')
        add_card = browser.find_element_by_class_name('m-icon__add-to-cart')
        add_card.click()
        shopping_card = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/a')
        shopping_card.click()
        shopping_card_list = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/a')
        shopping_card_list.click()
        shopping_card_delete = browser.find_element_by_link_text('კალათის გასუფთავება')
        shopping_card_delete.click()
        
