#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import time
import validators
import robobrowser
from random import choice
from werkzeug.utils import cached_property
from telegram import Bot, Update, User, Message
from telegram.ext import CommandHandler, Updater, MessageHandler, CallbackContext, Filters
from telegram.utils.request import Request
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

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
def start(update, context): # срабатывает на команду /start в телеграм чате
	update.message.reply_text("Вставьте URL из Coub")

@log_errors
def coub_scraper(update, context):
	USERAGENT = open("useragents.txt").read().split("\n")
	text_message = update.message.text

	if not validators.url(text_message):
		update.message.reply_text("Пожалуйста введите ссылку на Coub!")
	else:

		browser = robobrowser.RoboBrowser(
				user_agent=choice(USERAGENT), 
				parser='lxml'
			)
		browser.open(config.url)
		form = browser.get_form(action="/ru/web")
		form['url'].value = text_message
		browser.submit_form(form)

		for tag in browser.select('h3'):
			update.message.reply_text(tag.text)
	
def main():
	request = Request(
			connect_timeout=0.5, 
			read_timeout=1.0
		)
	bot = Bot(
			request=request, 
			token=config.token, 
			base_url=config.proxy #Подготовка прокси на случай блокировки ТГ. В конфиге поменять ссылку на прокси сервер
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