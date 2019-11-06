import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

chromedriver = "/Users/ssmoo/Downloads/chromedriver_win32/chromedriver"
#정치
f = open('segye_news_politics.txt', 'w', encoding='utf-8')
driver = webdriver.Chrome(chromedriver, chrome_options=options)
for i in range(1, 11):
    for j in range(1,21):
        try:
            driver.get("http://www.segye.com/newsList/0101010100000?curPage=" + str(i))
            click = '//*[@id="content"]/div[1]/div[1]/div[' +str(j) + ']/dl[2]/dt/a'
            driver.find_element_by_xpath(click).click()
            response = requests.get(str(driver.current_url))
            html = response.text
            
            soup = BeautifulSoup(html, 'html.parser')
            notices1 = soup.select('#content > div.news_article > div.article_head > div.subject > h1') #제목
            notices2 = soup.select('#article_txt') #기사
                                   
            for n in notices1:
                a = n.text.strip()
            for n in notices2:
                b = n.text.strip()
            
            b = str(b).replace("<연합>","")
            b = str(b).replace("\n", " ")
            
            f.write("정치" + "|" + str(a) + "|" + str(b) + "\n")
        except:
            pass
        
#경제
f = open('segye_news_economy.txt', 'w', encoding='utf-8')
driver = webdriver.Chrome(chromedriver, chrome_options=options)
for i in range(1, 11):
    for j in range(1, 21):
        try:
            driver.get("http://www.segye.com/newsList/0101030100000?curPage=" + str(i))
            click = '//*[@id="content"]/div[1]/div[1]/div[' +str(j) + ']/dl[2]/dt/a'
            driver.find_element_by_xpath(click).click()
            response = requests.get(str(driver.current_url))
            html = response.text
            
            soup = BeautifulSoup(html, 'html.parser')
            notices1 = soup.select('#content > div.news_article > div.article_head > div.subject > h1') #제목
            notices2 = soup.select('#article_txt') #기사
                                   
            for n in notices1:
                a = n.text.strip()
            for n in notices2:
                b = n.text.strip()
                
            b = str(b).replace("<연합>","")
            b = str(b).replace("\n", " ")
            
            f.write("경제" + "|" + str(a) + "|" + str(b)+ "\n")
        except:
            pass 

#연예
f = open('segye_news_entertainmnet.txt', 'w', encoding='utf-8')        
driver = webdriver.Chrome(chromedriver, chrome_options=options)
for i in range(1, 11):
    for j in range(1, 21):
        try:
            driver.get("http://www.segye.com/newsList/0101060100000?curPage=" + str(i))
            click = '//*[@id="content"]/div[1]/div[1]/div[' +str(j) + ']/dl[2]/dt/a'
            driver.find_element_by_xpath(click).click()
            response = requests.get(str(driver.current_url))
            html = response.text
            
            soup = BeautifulSoup(html, 'html.parser')
            notices1 = soup.select('#content > div.news_article > div.article_head > div.subject > h1') #제목
            notices2 = soup.select('#article_txt') #기사
                                   
            for n in notices1:
                a = n.text.strip()
            for n in notices2:
                b = n.text.strip()
 
            b = str(b).replace("<연합>","")
            b = str(b).replace("\n", " ")
            
            f.write("연예" + str(a) + "|" + str(b) + "\n")
        except:
            pass
        
#스포츠
f = open('segye_news_sport.txt', 'w', encoding='utf-8')        
driver = webdriver.Chrome(chromedriver, chrome_options=options)
for i in range(1, 11):
    for j in range(1, 21):
        try:
            driver.get("http://www.segye.com/newsList/0101110100000?curPage=" + str(i))
            click = '//*[@id="content"]/div[1]/div[1]/div[' +str(j) + ']/dl[2]/dt/a'
            driver.find_element_by_xpath(click).click()
            response = requests.get(str(driver.current_url))
            html = response.text
            
            soup = BeautifulSoup(html, 'html.parser')
            notices1 = soup.select('#content > div.news_article > div.article_head > div.subject > h1') #제목
            notices2 = soup.select('#article_txt') #기사
                                   
            for n in notices1:
                a = n.text.strip()
            for n in notices2:
                b = n.text.strip()

            b = str(b).replace("<연합>","")
            b = str(b).replace("\n", " ")
            
            f.write("스포츠" + str(a) + "|" + str(b) + "\n")
        except:
            pass
