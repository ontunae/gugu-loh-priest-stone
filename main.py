import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager

import time
import datetime
from datetime import date, timedelta

import plyer
from plyer import notification

import os



today = datetime.datetime.now()
yesterday = today - timedelta(1)
until = today.strftime('%Y-%m-%d')
since = yesterday.strftime('%Y-%m-%d')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://twitter.com/search?q=%EC%8B%A0%EB%B9%84%EC%83%81%EC%A0%90%2C%20%ED%94%84%EB%A6%AC%EC%8A%A4%ED%8A%B8%20until%3A" + until + "%20since%3A" + since + "&src=typed_query&f=live")
driver.implicitly_wait(10)


terminated = False

while not terminated:
    tweets = driver.find_elements_by_xpath("//article[@role='article']")

    if len(tweets) >= 3:
        notification.notify(
            title= '신비상점 안내',
            message = '신비상점에 프리스트 초월석/룬 등장!',
            app_name = '제작자: 이원',
            timeout = 10,
        )
        terminated = True
        driver.quit()
    else:
        time.sleep(600)
        driver.refresh()
