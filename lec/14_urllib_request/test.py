import requests
from time import sleep

# url ="https://api.telegram.org/bot941716973:AAHLtCFRXUuBe8eKFkPAPlEDnRoGjokFO5M
# /" #token's bot, наприклад, 
# url = "https://api.telegram.org/bot7068771712:AAFeQBh6MSQTLO5tBnbWk5Ny1CSadzIe2AY/"
url = "https://api.telegram.org/bot8634074443:AAGWwAYmzst5KsLw75fOs8L6KPPrXgoBdQQ/"

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
    # return results[-1]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response



def main():
    response=get_updates_json(url)
    last_update_resonce=last_update(response)
    print(last_update_resonce)
    update_id = last_update_resonce['update_id'] 
    last_message=last_update_resonce["message"]
    chat_id=get_chat_id(last_update_resonce)

    print(last_message)

    text=""
    if "text" in last_message.keys():
        text=last_message["text"]
        print(text)
    elif "photo" in  last_message.keys():
        print("photo")
        text="photo"

    # send_mess(chat_id,"Hi! Fine")
    send_mess(chat_id,text)


if __name__ == '__main__':
    main()
    # chat_id = get_chat_id(last_update(get_updates_json(url)))
    # send_mess(chat_id, 'Hello! How are you?')