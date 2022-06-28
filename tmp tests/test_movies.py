import unittest
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

class MoviesTestCase(unittest.TestCase):
    data = []

    def test_top_movies_find(self):
        for p in range(1, 6):

            print(p)
            url = 'https://www.kinopoisk.ru/lists/movies/top250/?page={p}'
            r = requests.get(url)
            sleep(15)

            soup = BeautifulSoup(r.text, "html.parser")

            movies = soup.findAll('div', class_='styles_root__ti07r')

            for movies in movies:
                links = "https://www.kinopoisk.ru/" + movies.find('a', class_='base-movie-main-info_link__YwtP1').get(
                    'href')
                name_us = movies.find('a', class_='base-movie-main-info_link__YwtP1').find('span',
                                                                                          class_='desktop-list-main-info_secondaryText__M_aus').text
                country = movies.find('a', class_='base-movie-main-info_link__YwtP1').find('span',
                                                                                          class_='desktop-list-main-info_truncatedText__IMQRP').text
                rate = movies.find('span',
                                  class_='styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg').text

                self.data.append([links, name_us, country, rate])

        headers = ['links', 'name_us', 'country', 'rate']

        df = pd.DataFrame(self.data, columns=headers)
        df.to_csv('/home/kali/data.csv', sep=';', encoding='utf8')



