import urllib.request as ur
# url='https://www.google.com.ua/'
url='https://api.escuelajs.co/api/v1/categories'
# connection_site=ur.urlopen(url)
# print(connection_site.status)
# print(connection_site.getheader('Content-Type'))
# data=connection_site.read()
# print(data)

# for key, value in connection_site.getheaders():
#     print(key,":", value)

import requests 
# url='https://www.google.com.ua/'

response=requests.get(url)
print(response.status_code)
print(response.headers)
for key, value in response.headers.items():
    print(key,":", value)
print(response.text)
