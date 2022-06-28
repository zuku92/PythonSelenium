import unittest
from selenium import webdriver
from time import sleep

class DeleteCardTestCase(unittest.TestCase):

    def test_delete(self):
        browser = webdriver.Chrome(executable_path='/home/kali/PycharmProjects/pythonselenium/chromedriver')
        browser.get('https://gorgia.ge/ka/')
        add_card = browser.find_element_by_class_name('m-icon__add-to-cart')
        add_card.click()
        card = browser.find_element_by_class_name('cm-tooltip')
        card.click()
        shopping_card = browser.find_element_by_class_name('ty-float-left')
        shopping_card.click()
        self.assertTrue('კერამოგრანიტი Clinker Brown 30*60' in browser.page_source)
        card_delete = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/div/div[2]/div/div/div/div/form/div[1]/div[1]/a[2]')
        card_delete.click()
        self.assertTrue('თქვენი კალათა ცარიელია' in browser.page_source)
        
        
