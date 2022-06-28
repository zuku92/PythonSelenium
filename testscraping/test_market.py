import unittest
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
import pandas as pd
from market_api import api


class MarketTestCase(unittest.TestCase):

    data = []

    """find products lists by api"""
    def test_market_products_list(self):

        browser = webdriver.Chrome(executable_path='/home/kali/PycharmProjects/pythonselenium/chromedriver')

        for p in api:

            url = 'https://2nabiji.ge/ge/search?searchText=' + str(p)
            browser.get(url)
            sleep(3)

        soup = BeautifulSoup(browser.page_source, 'html.parser')

        data_info = soup.find('div', 'Layout_contentWrapper__2kQSf').find('main', class_='fit').find('div','infinite-scroll-component__outerdiv').find('div', 'Search_search__result__3gGsu')

        el_len = len(data_info.findAll('div', 'ProductCard_container__1jtJF'))

        """sort and save product data source by name and price """

        for i in range(0, el_len):

            data_sourse = data_info.findAll('div', 'ProductCard_container__1jtJF')[i]

            tmp_name = data_sourse.find('div', class_='ProductCard_productInfo__21mxE')

            name = tmp_name.find('div', class_='ProductCard_title__rzbSG').text.strip()

            price = data_info.findAll('div', 'ProductCard_container__1jtJF')[i].find('div', class_='ProductCard_productInfo__price__2Ys9W').find('span').text.strip()

            self.data.append([name, price])

    """save product list"""
    def test_market_product_list_save(self):

        headers = ['name', 'price']

        df = pd.DataFrame(self.data, columns=headers)

        df.to_csv('/home/kali/PycharmProjects/pythonselenium/market_data.csv', sep=',', encoding='utf8')



