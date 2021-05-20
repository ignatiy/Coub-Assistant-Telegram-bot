#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import choice

from pathlib import Path

# Ссылка на страницу сайта который будем парсить с капчей
PAGE_URL = "https://coubassistant.com/"
# token BotFather
TOKEN = "1762361955:AAG2hiIZ9Bw7xYK5jm3yMyrbz8rrNMO2ufU"
# url api telegram или на прокси сервер
PROXY = "https://api.telegram.org/bot"
# Ключ от рукапчи из своего аккаунта https://rucaptcha.com
RUCAPTCHA_KEY = "ef35fba55008aae418ca908a27bd29b0"
# Google sitekey можно найти на странице coubassistant
SITE_KEY = "6Lej9tkaAAAAAKWusqMcrOeA-hpsHlgjXu-feuGF"
# Значение параметра action, которые вы нашли в коде сайта
ACTION = "homepage"
# Требуемое значение рейтинга (score) работника, от 0.1(робот) до 0.9(человечный человек)
MIN_SCORE = 0.8
# Заголовки
PATH = Path(Path.cwd(), 'headers', 'user-agent.txt')
USERAGENT = choice(open(f'{PATH}').read().split("\n")) if os.path.isfile(f'{PATH}') else 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
HEADERS = {
	'user-agent': USERAGENT,
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
	'accept-encoding': 'none'
}