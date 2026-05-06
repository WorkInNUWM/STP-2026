import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup 
import datetime


# url="https://bottlepy.org/docs/dev/"
# response=requests.get("https://bottlepy.org/docs/dev/")
# print(type(response.text))
# result_page=response.text
# soup=BeautifulSoup(result_page)
# # print(info)
# за назвою елемента
# get_a=soup.find_all('a')
# print(get_a)
# print("*"*50)
# list_links=[]
# for item in get_a:
#     list_links.append(item.text)
#     # print(item["href"])
#     print(item.get("href"))
#
# print(list_links)


# url="https://www.ukr.net/"
# #створити словник із списком останніх новин за категоріями
# response=requests.get(url)
#
# soup= BeautifulSoup(response.text,"html.parser")
# # category_info=soup.find("article",class_="feed")
# sections_news=soup.find_all("section",class_="feed_section")
# print(sections_news)

def parser_pogoda():
    """
        <div class="temperature">
          <div class="min">мін. <span>+14°</span></div>
         <div class="max">макс. <span>+25°</span></div>
        </div>

    """
    url = "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%80%D1%96%D0%B2%D0%BD%D0%B5/"
    date_now = datetime.datetime.now()
    url_date_now = f'{url}{date_now.date()}'
    print(url_date_now)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    response = requests.get(url_date_now, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # за селектором
        temperature_now = soup.select("div.main.loaded")[0]
        # print(temperature_now)
        block_temperature = temperature_now.find("div", class_="temperature")
        # print(block_temperature)
        temp_min = block_temperature.find("div", class_="min")
        # print(temp_min.span.string)
        # print(temp_min.span.text)
        temp_max = block_temperature.find("div", class_="max")
        # print(temp_max.span.string)
        temp_now = soup.find("p", class_="today-temp")
        # print(temp_now)
        text = f'Температура в Рівному на даний момент ствновить {temp_now.text}.\nMin: {temp_min.text}C. Max: {temp_max.text}C  '
        return text

def parsDollar():
    # Посилання на потрібну сторінку (ключове слово в google.com "долар")
    DOLLAR_GRN = 'https://www.google.com/search?rlz=1C1OKWM_ruUA876UA876&sxsrf=ALeKk006L1Pl75X-7g86W7rgWPHtCLIfcQ%3A1614235575840&ei=t0c3YIDtMsaIrwSkpLeoBQ&q=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80&oq=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAELEDMgUIABCxAzICCAAyBQgAELEDMgUIABDLATICCC4yBQgAELEDMgIIADICCAA6BwgjELADECc6BwgAELADEEM6BwguELADEENQwA9YwA9g2RBoAXACeACAAaEBiAGfApIBAzAuMpgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwjApNOQuITvAhVGxIsKHSTSDVUQ4dUDCA0&uact=5'
    # Заголовки для передачі разом з URL. Для отримання агента в пошуковачі набираємо "мій user  agent"
    # Отрмаємо:
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
    # парсим сторінку
    full_page = requests.get(DOLLAR_GRN, headers=headers)
    # Разбираємо через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Отримуєм потрібне значення
    # <span class="DFlfde SwHCTb" data-precision="2" data-value="27.946640000000002">27,95</span>
    value_dollar = soup.find("span", {"class": "DFlfde SwHCTb", "data-precision": 2})
    print(value_dollar["data-value"])
    current_converted_price = float(value_dollar.text.replace(",", "."))
    return value_dollar["data-value"]
if __name__=="__main__":
    print(parser_pogoda())
