import unittest
from selenium import webdriver
from time import sleep

class AddToCardTestCase(unittest.TestCase):

    def test_add_to_shopping_card(self):
        browser = webdriver.Chrome(executable_path='/home/kali/PycharmProjects/pythonselenium/chromedriver')

        browser.get('https://gorgia.ge/ka/')
        sleep(5)
        add_card = browser.find_element_by_xpath('//*[@id="button_cart_8900030701"]')
        add_card.click()
        shopping_card = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/a')
        shopping_card.click()
        shopping_card_list = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/a')
        shopping_card_list.click()
        self.assertIn('სამადგილიანი დივანი "MURPHY" (SAFIR GREY)', browser.page_source)
