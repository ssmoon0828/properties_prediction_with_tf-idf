# -*- coding: utf-8 -*-
"""
Created on Sun May  6 19:51:21 2018

@author: ssmoo
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

file = open('Music.csv', 'w', encoding='cp949', newline='')
wr = csv.writer(file)
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)
for i in range(1, 13):
    if len(str(i)) == 1:
        for j in range(1, 51):
            driver.get('http://www.mnet.com/chart/TOP100/20170' + str(i))
            click = '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[' + str(j) + ']/td[4]/div/div[2]/div[1]/a[1]'
            driver.find_element_by_xpath(click).click()
            response = requests.get(str(driver.current_url))
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            notices1 = soup.select('#content > div.music_info_view > ul > li.top_left > p')
            notices2 = soup.select(
                '#content > div.music_info_view > div.music_info_cont > dl > dd.title > span.artist_txt > a')
            notices3 = soup.select('#aside_rnb > div.hot_artist.pad_t15.pad_b10 > dl > dd > p.genre')
            notices4 = soup.select('#lyricsText')

            for n in notices1:
                a = n.text.strip()
            for n in notices2:
                b = n.text.strip()
            for n in notices3:
                c = n.text.strip()
            for n in notices4:
                d = n.text.strip()

            timeline = '20180' + str(i)
            wr.writerow([str(timeline), str(j), str(a), str(b), str(c), str(d)])
        i += 1
    else:
        for j in range(1, 51):
            driver.get('http://www.mnet.com/chart/TOP100/2017' + str(i))
            click = '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[' + str(j) + ']/td[4]/div/div[2]/div[1]/a[1]'
            driver.find_element_by_xpath(click).click()
            response = requests.get(str(driver.current_url))
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            notices1 = soup.select('#content > div.music_info_view > ul > li.top_left > p')
            notices2 = soup.select(
                '#content > div.music_info_view > div.music_info_cont > dl > dd.title > span.artist_txt > a')
            notices3 = soup.select('#aside_rnb > div.hot_artist.pad_t15.pad_b10 > dl > dd > p.genre')
            notices4 = soup.select('#lyricsText')

            for n in notices1:
                a = n.text.strip()
            for n in notices2:
                b = n.text.strip()
            for n in notices3:
                c = n.text.strip()
            for n in notices4:
                d = n.text.strip()

            timeline = '2018' + str(i)
            wr.writerow([str(timeline), str(j), str(a), str(b), str(c), str(d)])
        i += 1
file.close()