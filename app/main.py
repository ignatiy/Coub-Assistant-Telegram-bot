#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from random import choice

import validators
import robobrowser
from werkzeug.utils import cached_property
from telegram import Bot, Update, User, Message
from telegram.ext import CommandHandler, Updater, MessageHandler, CallbackContext, Filters
from telegram.utils.request import Request
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from python_rucaptcha import ReCaptchaV3

import config

def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e
    return inner

@log_errors
def start(update, context):
	update.message.reply_text("Вставьте URL из Coub")

@log_errors
def coub_scraper(update, context):

	answer_usual_re3_f = ReCaptchaV3.ReCaptchaV3(
		rucaptcha_key=config.RUCAPTCHA_KEY,
		action=config.ACTION,
		min_score=config.MIN_SCORE).captcha_handler(site_key=config.SITE_KEY, page_url=config.PAGE_URL)

	if not answer_usual_re3_f["error"]:
		USERAGENT = open("useragents.txt").read().split("\n")
		text_message = update.message.text

		if not validators.url(text_message):
			update.message.reply_text("Пожалуйста введите ссылку на Coub!")
		else:

			browser = robobrowser.RoboBrowser(
					user_agent=choice(USERAGENT), 
					parser='lxml'
				)
			browser.open(config.PAGE_URL)
			form = browser.get_form(action="/ru/web")
			form['url'].value = text_message
			form['token'].value = answer_usual_re3_f["captchaSolve"]
			browser.submit_form(form)

			for tag in browser.select('h3'):
				update.message.reply_text(tag.text)
	elif answer_usual_re3_f["error"]:
		update.message.reply_text("Что-то пошло не так..")
	
def main():
	request = Request(
			connect_timeout=0.5, 
			read_timeout=1.0
		)
	bot = Bot(
			request=request, 
			token=config.TOKEN, 
			base_url=config.PROXY
		)
	updater = Updater(
			bot=bot, 
			use_context=True
		)
	response = updater.bot.get_me()

	print('*' * 30)
	start_message = f'Start: {response.username}'
	print(start_message)
	
	dispatcher = updater.dispatcher
	dispatcher.add_handler(CommandHandler("start", start))
	dispatcher.add_handler(MessageHandler(Filters.text, coub_scraper))

	updater.start_polling()
	updater.idle()
	
	print('\nFinish telegram\n')

if __name__ == '__main__':
	main()