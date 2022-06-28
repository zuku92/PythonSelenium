import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ApiTestCase(unittest.TestCase):

    url = 'https://2nabiji.ge/'

    """api test"""

    def test_api(self):

        browser = requests.get(self.url)

        self.assertEqual(200, browser.status_code)


    def test_search(self):
        browser = webdriver.Chrome(executable_path='/home/kali/PycharmProjects/pythonselenium/chromedriver')
        browser.get(self.url)
        search_field = browser.find_element_by_xpath('// *[ @ id = "search"]')
        search_field.send_keys('პური', Keys.RETURN)

        self.assertTrue('პური' in browser.page_source)



    






