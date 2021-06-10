#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os

from selenium import webdriver
from bs4 import BeautifulSoup
from pathlib import Path

path = Path(Path.cwd(), 'drivers', 'chromedriver')

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.headless = True

driver = webdriver.Chrome(executable_path=path, options=options)
driver.get("https://coubassistant.com/")

form = driver.find_element_by_xpath("//input[@placeholder='Вставьте URL из Coub']").send_keys('https://coub.com/view/2pqvpf')
time.sleep(3.048)
button = driver.find_element_by_xpath("//input[@value='Искать']").click()
time.sleep(1.05)
res = driver.page_source
# print(res)

soup = BeautifulSoup(res, 'lxml').select('h3')[0].get_text()
# print(soup)

if not soup:
	# print(soup)
	print("Что-то не так")
	driver.close()
else:
	print(soup)
	# print("Что-то не так")
	driver.close()