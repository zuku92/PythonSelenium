
import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver



class SearchTestCase(unittest.TestCase):

    def setUp(self) -> None:

        self.browser = webdriver.Chrome(executable_path='/home/kali/PycharmProjects/pythonselenium/chromedriver')


    
    def test_search(self):

    	browser = self.browser
    	browser.get('https://gorgia.ge/ka/')
    	search = browser.find_element_by_name('hint_q')
    	search.send_keys('სავარძელი')
    	search.send_keys(Keys.RETURN)
    	self.assertTrue('სავარძელი' in browser.page_source)
    	self.assertIn("ნაპოვნი პროდუქტი: 108", browser.page_source)



    
        
       
        
       
	




