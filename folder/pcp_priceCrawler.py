from selenium import webdriver
from csv import DictReader
from datetime import *
import time
from bs4 import BeautifulSoup
import csv
import random


def get_cookies_values(file):
    with open(file, encoding='utf-8-sig') as f:
        dict_reader = DictReader(f)
        list_of_dicts = list(dict_reader)
    return list_of_dicts


def chromebrowser(url, driver, recordno):
    print('-------------------------------------------------------------------------------------------------------')
    print("Sleeps for random seconds between 2 to 3")
    print(f'Recordno:{recordno}')
    time.sleep(random.choice(range(2,3)))
    driver.get(url)
    print("Sleeps for 5 secs")
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    try:
        title = soup.title.text.strip()
    except:
        title = ''
    if title != 'Just a moment...':
        pass
    else:
        print('Time to change cookie')
        print(input('Wait you have got a security check'))
        cookies = get_cookies_values('pcp_ch_cookies.csv')
        for i in cookies:
            driver.add_cookie(i)
        driver.refresh()

        soup = BeautifulSoup(driver.page_source, 'lxml')

    return soup


def get_product(soup, url, recordno):
    print(url)
    dat = date.today()
    try:
        mpn = soup.find('span', class_='manufacturerItem').span.text.strip()
    except:
        mpn = ''
    try:
        price = soup.find('div',
                          class_='containerPrices sm-flex lg-flex sm-wrap lg-wrap sm-dir-col lg-dir-row lg-j-end').div.text.replace(
            "'", ",").strip()
    except:
        price = ''
    try:
        notification = soup.find('div', {'id': 'notification'}).h3.text.replace(
            "Diesen Artikel können wir leider nicht mehr für Sie bestellen.",
            "Unfortunately, we can no longer order this item for you.").strip()
    except:
        notification = ''
    print(mpn)
    print(price)
    print(notification)
    print('inc')
    timestamp = datetime.utcnow().strftime("%m/%d/%Y %H:%M:%S")
    with open('pcp_PriceCollector_' + str(dat) + '.csv', 'a', newline='', encoding='utf-8-sig') as fp:
        writer = csv.writer(fp)
        writer.writerow(
            [recordno, url, mpn, price, notification, 'inc', 'In Stock',
             timestamp
             ])


def main():
    try:
        recordno = 0
        dat = date.today()
        with open('pcp_PriceCollector_' + str(dat) + '.csv', 'a', newline='', encoding='utf-8-sig') as fp:
            writer = csv.writer(fp)
            writer.writerow(
                ['Record_no', 'link', 'MPN', 'price', 'Notification', 'Inc/excl', 'stock', 'Timestamp'],
            )
        week = (datetime.today()).strftime('%U')
        week = int(week) - 12

        contents = []
        with open('data.csv', 'r') as f:
            urls = csv.reader(f)
            for url in urls:
                contents.append(url[0])

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        base_url = 'https://www.steg-electronics.ch/de/product/lenovo-thinkpad-x1-titanium-yoga-gen-1-13-5-qhd-i7-16gb-512gb-ssd-intel-iris-xe-w10p-28145369'
        driver.get(base_url)
        print(input('wait,Proxy entered'))
        cookies = get_cookies_values('pcp_ch_cookies.csv')
        for i in cookies:
            driver.add_cookie(i)
        driver.refresh()
        time.sleep(2)
        input('captcha bypassed?')

        for url in contents:
            recordno += 1
            soup = chromebrowser(url, driver,recordno)
            get_product(soup, url, recordno)


        driver.close()

    except Exception as e:
        print(e)
        dat = date.today()
        with open('pcp_priceCollector_pnf_' + str(dat) + '.csv', 'a', encoding='utf-8-sig') as fp:
            writer = csv.writer(fp)
            writer.writerow(
                [url, str(e)]
            )


if __name__ == '__main__':
    main()
