"""
Багаторядковий 
коментар
"""

str1="We are lerning "
print(id(str1))
str2="Python/C#!"
str1+=str2
print(str1)
print(id(str1))

message="We are вивчаємо Python" # визначення рядка
print(message[1])
# message[1]="f" #ERROR TypeError: 'str' object does not support item assignment
print(ord("a"))
print(chr(65))
message1=message.encode('utf-8')
print(message.encode('utf-8'))
print("абвг".encode('utf-8'))
# # 11010000
print(message1.decode('utf-8'))
str1=r"C:\temp\new"
print(str1)
s="this is a text"
print("id=",id(s))
# print(s[0])
# #s[0]="T" #error
# s="T"+s[1:]
s=s.capitalize()
print(s)
print("id=",id(s))
print(s*6)
print(s[::-1])
print(s[::2])
print(s[5:2:1])


import string
# # """
# # Дано рядок. Виконайте наступні дії із рядком:
# # """
symbols = 'abcdefghijklmnopqrstuvwxyz'
symbols=string.ascii_lowercase
print(symbols)
print(f"len({symbols})={len(symbols)}")
# # #1) Спочатку виведіть третій символ цього рядка.
# print(symbols[2]) # 'c'
# # #2) У другому рядку виведіть передостанній символ цього рядка.
# # #str[start:end:step]
# print(symbols[-2]) # 'y'
# length=len(symbols)
# print(symbols[length-2]) # 'y'
# # #3) У третьому рядку виведіть перші п'ять символів цього рядка.
# print(symbols[:5])
# print(symbols[-length:-length+5])  #-26 :-21
# # #4) У четвертому рядку виведіть весь рядок, крім останніх двох символів.
# print(symbols[:-2])
# # #5) У п'ятому рядку виведіть всі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться починаючи з першого).
# print(symbols[1::2])
# # #6) У шостому рядку виведіть всі символи з непарними індексами, тобто починаючи з другого символу рядка.
# print(symbols[::2])
# # #7) У сьомому рядку виведіть всі символи в зворотному порядку.
# print(symbols[::-1])  # 0 + -1 , -2, -3
# # #8) У восьмому рядку виведіть всі символи рядка через один в зворотному порядку, починаючи з останнього.
# print(symbols[-1::-2])
# # #9) У дев'ятому рядку виведіть довжину цього рядка.

print("456.4".isdigit())
print("456".isdecimal())
print("4564.5".isalnum())
s=["true","false"]
new_str=";".join(s)
print(new_str)
print(new_str.upper())

for symbol in "Python":
    print(symbol)

print(message.swapcase())
a=4.567
b=-75656
str_result="Expretions: {}/{}={:10_}".format(a,b,a/b)
print(str_result)
str_result="Expretions: {1}*{0}={2:_>10.3f}".format(a,b,a*b)
print(str_result)

"""
Знайти всі входження рядка "ми" в заданий рядок 
"""

str2="Ми сьогодні вивчали рядки. Ми трохи зрозуміли,  а ми - трохи ні!"
index1=str2.lower().find("ми")
count=0
while index1!=-1:
    count+=1
    # if count==2:
    #     break
    print(index1)
    index1=str2.lower().find("ми",index1+1)
else:
    print(f"Worked block else count 'ми' =>{count}")

print(f"count 'ми' =>{count}")

# from string import Formatter
# from string import Template

# formatter=Formatter()
# print(formatter.format('{userLog}',userLog='Admin'))
# print(formatter.format('{} {userLog}','Welcome, ',userLog='Admin'))
# print('{} {userLog}'.format('Welcome, ',userLog='Admin'))

# # using Template
# # шаблон
# temp_str=Template('$userName has $ageUser. Welcome!')

# #використання шаблону
# resultStr=temp_str.substitute(userName="Admin",ageUser=23) # str=object
# print(resultStr)

# # find(), index()
# # reuglar expressions, regex, RE

# import re
# # re.search()
# # re.findall()
# # re.match()
# # знайти у рядку слово, що  складається з 4-х символів літер і цифр.
# userStr="abcd df ghghg"
# match1=re.search(r"\w{4}",userStr)
# print(match1.group()) #abcd
# print(match1.group(0)) #abcd
# userStr="abcd df345 567 ghghg"
# match1=re.search(r"\d{3}",userStr)
# print(match1.group()) #abcd

# #dd.mm.yyyy
# userStr2="2024-2025 Exam: 14.12.2024 - Python, 18.12.2024 - Operation System" 
# match2=re.findall(r'\d{2}.\d{2}.\d{4}',userStr2)
# print(match2)

# # using re.match()
# str3="My phones: Kyivstar +38(067)345-67-89, Vodafone +38(095)376-87-89 "
# # /\+38\(067\)(\d\d\d-\d\d-\d\d)/gm
# match1= re.search(r'\+38\(067\)(\d\d\d-\d\d-\d\d)',str3)
# print(match1.group())
# str4="My phones: Kyivstar +38(067)345-67-89, Vodafone +38(095)376-87-89"
# match1= re.search(r'Kyivstar \+38\(067\)(\d\d\d-\d\d-\d\d), Vodafone \+38\(095\)(\d\d\d-\d\d-\d\d)',str4)
# print(match1.group())
# print(match1.group(0))
# print(match1.group(1))
# print(match1.group(2))
# print(match1.group(1,2))
# print(len(str4))
# print(match1.start(),match1.end())
# str5="My phones: Kyivstar +38(067)345-77-89, Vodafone +38(095)376-89-89"
# str6="Kyivstar +38(067)345-88-89, Vodafone +38(095)376-98-89"
# match4= re.match(r'Kyivstar \+38\(067\)(\d\d\d-\d\d-\d\d), Vodafone \+38\(095\)(\d\d\d-\d\d-\d\d)',str5)
# match5= re.match(r'Kyivstar \+38\(067\)(\d\d\d-\d\d-\d\d), Vodafone \+38\(095\)(\d\d\d-\d\d-\d\d)',str6)

# print(match4) #None
# print(match5.group()) #Kyivstar +38(067)345-88-89, Vodafone +38(095)376-98-89



# userStr3="2024-2025 Exam: 14.12.2024 - Python, 18.12.2024 - Operation System" 
# newStr=re.sub(r'[-,]','/',userStr3)
# print(newStr)
# newStr=re.sub(r'\.','/',userStr3)
# print(newStr)
# newStr=userStr3.replace(".","/")
# print(newStr)
