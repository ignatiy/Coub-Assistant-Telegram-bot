#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import choice

from pathlib import Path

# Ссылка на страницу сайта который будем парсить
PAGE_URL = "https://coubassistant.com/"
# token BotFather
TOKEN = "1762361955:AAG2hiIZ9Bw7xYK5jm3yMyrbz8rrNMO2ufU"
# url api telegram или на прокси сервер
PROXY = "https://api.telegram.org/bot"
# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent
# Пользовательский агент
PATH_HEADERS = BASE_DIR / 'headers' / 'user-agent.txt'
USERAGENT = choice(PATH_HEADERS.read_text().splitlines()) if PATH_HEADERS.is_file() else 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
# cromedriver
PATH_DRIVERS = BASE_DIR / 'drivers' / 'chromedriver'
DRIVERS = PATH_DRIVERS if PATH_DRIVERS.is_file() else os.path.abspath('/media/hdd/Project/Coub-Assistant-Telegram-bot/app/drivers/chromedriver')