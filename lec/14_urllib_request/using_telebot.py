import requests
#pip install requests
import telebot
#pip install pytelegrambotapi
import os
from  telebot import types
# import  using_bs4
# from bs4 import BeautifulSoup

# tocken="1601733261:AAFewQtugTk9vzIHyQMa524wH20znCZqWFw"
tocken="1601733261:AAFewQtugTk9vzIHyQMa524wH20znCZqWFw"
# бот AAP_CT_bot
tocken="7068771712:AAFeQBh6MSQTLO5tBnbWk5Ny1CSadzIe2AY"
bot = telebot.TeleBot(tocken)

@bot.message_handler(commands=['start', 'help']) # /start  /help
def send_welcome(message):
	bot.send_message(message.chat.id, "{},як справи? Надішлеш мені якесь фото?".format(message.chat.first_name))
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.send_message(message.chat.id, message.text)

#Для демонстрації роботи із фото даний метод надсилає назад фото і як відповідь завантажує файл на диск
# @bot.message_handler(content_types=['photo'])
# def handle_photo(message):
#     # доступаємося до файла на сервері
#     print(message.photo)
#     file_info = bot.get_file(message.photo[-1].file_id)
#     print(file_info)
#     # бот відправляє користувачу наіслане ним фото назад
#     bot.send_photo(message.chat.id, message.photo[-1].file_id)
#
#     #завантажуємо файл із сервера із використанням методів модуля telebot
#     downloaded_file = bot.download_file(file_info.file_path)
#     # це еквівалентно використанню модуля requests двом командам (це якщо навіть не використовувати модулі для роботи з API телеграм):
#     # 1) file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(tocken, file_info.file_path))
#     # 2) downloaded_file=file.content
#
#     #шлях до папки, наприклад, "D:/2020_2021/"+"photos/назва файлу", тому обовязково
#     # потрібно створити папку photos в папці D:/2020_2021/
#     #src = 'D:\\2023_2024\\' + file_info.file_path
#     # with open(src, 'wb') as new_file:
#     #     new_file.write(downloaded_file)
#     bot.reply_to(message, "Прийнято і завантажено! Фото завантажено на диск!:)")

@bot.message_handler(commands=['sitefmi'])
def send_infoUrlFmi(message):
	urlFMI="http://fmi-rshu.org.ua/"
	text=f'Сайт твого факультету доступний за посиланням <a href="{urlFMI}">Сайт ФМІ</a>'
	bot.send_message(message.chat.id, text,parse_mode='html')

@bot.message_handler(content_types=['photo'])
def send_photos(message):
	print(message)
	file_info=bot.get_file(message.photo[-1].file_id)
	print(file_info)
	downloaded_file=bot.download_file(file_info.file_path)
	bot.send_photo(message.chat.id,message.photo[-1].file_id)
	src = 'E:/' + file_info.file_path;
	with open(src, 'wb') as new_file:
		new_file.write(downloaded_file)
	bot.reply_to(message,"Фото завантажене")

@bot.message_handler(commands=['menu'])
def send_menu(message):
	murkup=types.InlineKeyboardMarkup()
	btn1=types.InlineKeyboardButton("Погода в Рівному",callback_data="parsPogoda")
	btn2 = types.InlineKeyboardButton("Курс долара", callback_data="parsDollar")
	murkup.add(btn1,btn2)
	bot.send_message(message.chat.id,"Виберіть пункт меню:",parse_mode='html',reply_markup=murkup)

@bot.callback_query_handler(func=lambda call:True)
def callback_woker(call):
	text_msg="None"
	# print(call.data)
	# print(parsPogoda())
	if call.data=="parsPogoda":
		# text_msg=using_bs4.parser_pogoda()
		pass
	elif call.data=="parsDollar":
		# text_msg = using_bs4.parsDollar()
		pass
	bot.send_message(call.message.chat.id, text_msg)



bot.polling()