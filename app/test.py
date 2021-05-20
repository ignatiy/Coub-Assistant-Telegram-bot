#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from random import choice

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
	browser.open(config.PAGE_URL)
	form = browser.get_form(action="/ru/web")
	form['url'].value = "https://coub.com/view/2s33vc"
	form['token'].value = answer_usual_re3_f["captchaSolve"]
	browser.submit_form(form)

	for tag in browser.select('h3'):
		print(tag.text)

elif answer_usual_re3_f["error"]:
	print("Что-то пошло не так..")