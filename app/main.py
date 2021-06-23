#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import validators
from selenium import webdriver
from bs4 import BeautifulSoup
# from werkzeug.utils import cached_property
from telegram import Bot, Update, User, Message
from telegram.ext import CommandHandler, Updater, MessageHandler, CallbackContext, Filters
from telegram.utils.request import Request
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

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
	text_message = update.message.text

	if not validators.url(text_message):
		update.message.reply_text("Пожалуйста введите ссылку на Coub!")
	else:
		options = webdriver.ChromeOptions()
		options.add_argument(config.USERAGENT)
		options.add_experimental_option("excludeSwitches", ["enable-automation"])
		options.add_experimental_option("useAutomationExtension", False)
		options.add_argument("--disable-blink-features=AutomationControlled")
		options.add_argument("--no-sandbox")
		options.headless = True

		driver = webdriver.Chrome(executable_path=config.DRIVERS, options=options)
		driver.get(config.PAGE_URL)
		form = driver.find_element_by_xpath("//input[@placeholder='Вставьте URL из Coub']").send_keys(text_message)
		time.sleep(1.58)
		button = driver.find_element_by_xpath("//input[@value='Искать']").click()
		time.sleep(1.15)
		res = driver.page_source
		
		soup = BeautifulSoup(res, 'lxml').select('h3')[0].get_text()
		
		if not soup:
			update.message.reply_text("Что-то пошло не так")
			driver.close()
			driver.quit()
		else:
			update.message.reply_text(soup)
			driver.close()
			driver.quit()

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