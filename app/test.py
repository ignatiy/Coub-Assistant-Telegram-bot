#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from random import choice

import asyncio
import requests
import validators
import robobrowser
from werkzeug.utils import cached_property
from telegram import Bot, Update, User, Message
from telegram.ext import CommandHandler, Updater, MessageHandler, CallbackContext, Filters
from telegram.utils.request import Request
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from python_rucaptcha import ReCaptchaV3

import config

answer_usual_re3_f = ReCaptchaV3.ReCaptchaV3(
		rucaptcha_key=config.RUCAPTCHA_KEY,
		action=config.ACTION,
		min_score=config.MIN_SCORE).captcha_handler(site_key=config.SITE_KEY, page_url=config.PAGE_URL)

if not answer_usual_re3_f["error"]:
	# USERAGENT = open("useragents.txt").read().split("\n")

	browser = robobrowser.RoboBrowser(history=True)
	s = requests.Session()
	s.headers = config.HEADERS
	# browser = RoboBrowser(session=s, parser='lxml')
	
	browser = robobrowser.RoboBrowser(
			session=s, 
			parser='lxml'
		)
	browser.open(config.PAGE_URL, proxies={'http': 'http://172.67.181.166:80'})
	form = browser.get_form(action="/ru/web")
	# time.sleep(3)
	form['url'].value = "https://coub.com/view/2s33vc"
	form['token'].value = answer_usual_re3_f["captchaSolve"]
	time.sleep(5)
	browser.submit_form(form)
	# time.sleep(5)

	for tag in browser.select('h3'):
		print(tag.text)

elif answer_usual_re3_f["error"]:
	print("Что-то пошло не так..")

# async def run():
#     try:
#         answer_aio_re3 = await ReCaptchaV3.aioReCaptchaV3(
#         	rucaptcha_key=config.RUCAPTCHA_KEY,
#         	action=config.ACTION,
#         	min_score=config.MIN_SCORE).captcha_handler(site_key=config.SITE_KEY, page_url=config.PAGE_URL)
#         if not answer_aio_re3["error"]:
#             # решение капчи
#             print(answer_aio_re3["captchaSolve"])
#             print(answer_aio_re3["taskId"])
#             print(answer_aio_re3["user_check"])
#             print(answer_aio_re3["user_score"])
#         elif answer_aio_re3["error"]:
#             # Тело ошибки, если есть
#             print(answer_aio_re3["errorBody"])
#     except Exception as err:
#         print(err)


# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(run())
#     loop.close()