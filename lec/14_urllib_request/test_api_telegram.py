# pip install requests
import requests
# import json
from time import  sleep
# бот AAP_CT_bot
# tocken="7068771712:AAFeQBh6MSQTLO5tBnbWk5Ny1CSadzIe2AY"
tocken="8634074443:AAGWwAYmzst5KsLw75fOs8L6KPPrXgoBdQQ"
# https://api.telegram.org/bot<token>/METHOD_NAME
url=f"https://api.telegram.org/bot{tocken}/"
urlFile=f"https://api.telegram.org/file/bot{tocken}/getFile?"
# print(url)
def get_updates_json(request):
    # параметри для отримання оновлень через API для довгих опитуваннь (long polling),
    # без цих параметрів будуть короткі опитування (short polling)
    params = {'timeout': 100, 'offset': None}
    response=requests.get(request+'getUpdates', data=params)
    return response.json()

def last_update(data):
    results=data['result']
    if len(results) > 0:
        last_update = results[-1]
    else:
        last_update = results[len(results)]
    return last_update

def get_chat_id(update):
    chat_id=update['message']['chat']['id']
    return chat_id

#response BOT
def send_message(chat,text):
    parametrs={'chat_id':chat,'text':text}
    response=requests.post(url+'sendMessage',data=parametrs)
    return response

def send_photo(chat_id,path_photo):
    # data = {'chat_id': str(chat_id)}
    file = {'photo': open(path_photo, 'rb')}
    # response=requests.post(url+'sendPhoto?chat_id=' + data['chat_id'], files=file)
    response=requests.post(url+'sendPhoto?chat_id=' + str(chat_id), files=file)
    sleep(1)
    # response=requests.get(f"https://api.telegram.org/bot7068771712:AAFeQBh6MSQTLO5tBnbWk5Ny1CSadzIe2AY/sendPhoto?chat_id={chat}&file_id={photo}")
    return response

if __name__ == "__main__":
    update_id=last_update(get_updates_json(url))["update_id"]
    if update_id!=None:
        # print(update_id)
        sleep(2)
        while True:
            response_current=last_update(get_updates_json(url))
            current_id=response_current["update_id"]
            print(current_id)
            print(update_id)
            print("================")
            if update_id==current_id:
                chat_id = get_chat_id(response_current)
                if "text" in response_current["message"]:
                    result_text_updates=str(response_current["message"]["text"])
                    user_name=response_current["message"]["from"]["first_name"]
                    answer_bot=""
                    if result_text_updates.lower() in ["hello", "hi", "привіт"]:
                        answer_bot=f"Привіт, {user_name}"
                    # print(result_text_updates)
                    send_message(chat_id,answer_bot)
                    # send_message(chat_id,result_text_updates)
                    update_id+=1
                elif "photo" in response_current["message"]:
                    photo=response_current["message"]["photo"]
                    print(photo[-1]["file_id"])
                    file_id=photo[-1]["file_id"]
                    print(photo[-1])
                    fileInfo=requests.get('https://api.telegram.org/bot{0}/getFile?file_id={1}'.format(tocken, file_id))
                    # print(fileInfo.json())
                    # print(fileInfo.json()["result"]["file_path"])
                    # https://api.telegram.org/file/bot7068771712:AAFeQBh6MSQTLO5tBnbWk5Ny1CSadzIe2AY/photos/file_1.jpg
                    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(tocken, fileInfo.json()["result"]["file_path"]))
                    print(file)
                    downloaded_file=file.content
                    # print(file.content)
                    # E:\Tetiana\CT_Python_2023_2024\semestr_IV\08_urllib_request\AgACAgIAAxkBAAOjZk5kPv
                    # path = "E:\\Tetiana\\CT_Python_2023_2024\\semestr_IV\\08_urllib_request\\"+photo[-1]["file_id"]+".jpg"
                    path = "E:\\Tetiana\\CT_Python_2023_2024\\semestr_IV\\08_urllib_request\\resend.jpg"
                    with open(path,'wb') as new_file:
                        new_file.write(downloaded_file)
                    # sleep(1)
                    send_photo(chat_id,path)
                    update_id+=1
            sleep(4)



# Надсилання файлів
# Боти Telegram можуть надсилати файли трьома способами:
# Через file_id, тобто відправивши файл за допомогою ідентифікатора, який уже відомий боту.
# Через URL-адресу, тобто передаючи загальнодоступну URL-адресу файлу, яку Telegram завантажує та надсилає для вас.
# Через завантаження власного файлу.
# У всіх випадках методи, які потрібно викликати, мають однакові назви. Залежно від того, який із трьох способів ви оберете для надсилання файлу, параметри цих функцій відрізнятимуться. Наприклад, щоб надіслати фотографію, ви можете використати ctx.replyWithPhoto або sendPhoto, якщо ви використовуєте ctx.api або bot.api.
# Ви можете надсилати інші типи файлів, просто перейменувавши метод і змінивши тип даних, які ви йому передаєте. Щоб надіслати відео, ви можете використовувати ctx.replyWithVideo. Так само й для документа: ctx.replyWithDocument. Ну, ідею ви зрозуміли.
# Давайте розглянемо три способи надсилання файлу.