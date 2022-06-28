import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumTestCase(unittest.TestCase):



    def test(self):

        url = 'http://tutorialsninja.com/demo/'

        browser = webdriver.Chrome(executable_path="/home/kali/PycharmProjects/pythonselenium/chromedriver")
        browser.get(url)

        search_field = browser.find_element_by_name('search')
        search_field.send_keys('iphone')
        search_field.send_keys(Keys.RETURN)
        add_to_card_button = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/div[2]/div[2]/button[1]')
        add_to_card_button.click()
        shopping_card_link = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]')
        shopping_card_link.click()


        self.assertTrue( 'product 11' in self.browser.page_source)
        browser.close()


























