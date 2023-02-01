import csv
import random
from datetime import *
import time
from lxml import html
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service


class Amazon_ae():
    def __init__(self):
        self.product()

    def is_next(self, soup):
        try:
            href_tags = soup.find('a', class_="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator")\

            if href_tags.text.strip() == "Next":
                url = 'https://www.amazon.ae' + href_tags['href'].strip()
                return url
        except:
            return False

    def product(self):
        dat = date.today()
        with open('Amazon_ae_' + str(dat) + '.csv', 'a', newline='', encoding='UTF-8-SIG') as fp:
            writer = csv.writer(fp)
            writer.writerow(
                ['PageNumber','Record_no','Category','Website','Country','Name','Description','Brand','MPN','producturl','Timestamp','Cachepage'], )
        week = (datetime.today()).strftime('%U')
        week = int(week) - 12
        base_url ='https://www.amazon.ae/s?i=computers&rh=n%3A12050245031&fs=true&page=2&qid=1647872572&ref=sr_pg_2'
        print('Opening Chrome Browser Automatically in 5 secs')
        time.sleep(5)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(r'E:\System Pricing\py\supportingfiles\chromedriver.exe')
        driver = webdriver.Chrome(options=options, service=service)
        print(
            'Browser Opened successfully ,Please Enter Proxy in browser for authentication manually So we can connect you '
            'with base url')
        driver.get(base_url)
        print(input("Stopper for entering Proxies- Manually (Y/N): "))
        print(f'Base url opened in browser: {base_url}')
        recordno = 0
        category_counter = 0
        list_urls = ['https://www.amazon.ae/s?i=computers&rh=n%3A12050245031&fs=true&page=1&qid=1653041716&ref=sr_pg_2',
                    'https://www.amazon.ae/s?i=computers&rh=n%3A15387140031&fs=true&page=1&qid=1653048770&ref=sr_pg_2'
                    ]

        for url in list_urls:
            category_counter += 1
            if category_counter == 1:
                category = 'Laptop'
            else:
                category = 'Desktop'
            try:
                pageno = 0
                print()
                pageurl = url
                while True:
                    pageno += 1
                    print()
                    print('---------Page change is in process ,Time in Seconds will be selected randmonly between '
                          f'10-15,pageno: {pageno} ,url will be printed shortly on screen--------------')
                    time.sleep(random.choice(range(2,5)))

                    print(f'Url: {pageurl}')
                    print('Sleep Time')
                    driver.get(pageurl)
                    time.sleep(random.choice(range(5,8)))
                    soup = BeautifulSoup(driver.page_source, 'lxml')
                    for item in soup.find_all('div',class_='a-section a-spacing-base'):
                        recordno = recordno + 1
                        print(f'--------------------------------Page{pageno}-----------------------------------------')
                        print(f'Current Category running: {category}')
                        print(recordno)
                        try:
                            name = item.find('div',
                                             class_='a-section a-spacing-small puis-padding-left-small puis-padding-right-small').h2.a.span.text.strip()
                        except:
                            try:
                                name = item.find('div',
                                                 class_='a-section a-spacing-micro puis-padding-left-small puis-padding-right-small') \
                                    .h2.a.span.text.strip()
                            except:
                                name = ''
                        print(name)

                        try:
                            link = item.find('div',
                                             class_='a-section a-spacing-small puis-padding-left-small puis-padding-right-small').h2.a.get(
                                'href')
                        except:
                            try:
                                link = item.find('div',
                                                 class_='a-section a-spacing-micro puis-padding-left-small puis-padding-right-small').h2.a.get(
                                    'href')
                            except:
                                link = ''
                        try:
                            final_link = f'https://www.amazon.ae{link}'
                        except:

                            final_link = ''
                        print(final_link)

                        timestamp = datetime.utcnow().strftime("%m/%d/%Y %H:%M:%S")
                        with open('Amazon_ae_' + str(dat) + '.csv', 'a', newline='', encoding='UTF-8-SIG') as fp:
                            writer = csv.writer(fp)
                            writer.writerow(
                                [pageno, recordno, category, 'amazon.ae', 'United Arab Emirates', name,'','','',final_link,
                                 timestamp,
                                 ''])
                    pageurl = self.is_next(soup)
                    if not pageurl:
                        break
            except Exception as e:
                with open('Amazon_ae__PNF_' + str(dat) + '.csv', 'a', newline='', encoding='UTF-8-SIG') as fp:
                    writer = csv.writer(fp)
                    writer.writerow(
                        [url, str(e)])
        print('------------------- Everthing went well, If any error, check exception--------------')
        time.sleep(2)
        print(
            '------------------- Initiating procedure to close Chrome Browser in 5 secs ----------------------')
        time.sleep(5)
        driver.quit()
        print('Browser Closed')

obj = Amazon_ae()


