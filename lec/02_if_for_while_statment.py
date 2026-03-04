# # # if value:
# # #     commands
# # # else:
# # #     commands

# # # if value1:
# # #     commands
# # # elif value2:
# # #     commands
# # # else:
# # #     commands

# # # # #> < >= <= != is  and or not
# # # # # predicate , logic value


if "Python": #true
    print("Commands for true")
else:
    print("Commands for false")


if not None: #  23, "str", 2>1 =>  true
    print("Commands for true")
else:
    print("Commands for false")

a=4
b=6
if a>b:
    max=a
else:
    max=b
print("max=",max,sep="",end="; ")
print(max,"**2=",max**2, sep="")
text=f"{max}**2={max**2}"
print(text)
# # print(f'max={max}')
# # text2="max={:d}".format(max)
# # print(text2)

# # # # # operand1 if value else operand2
max=a if a>b else b #ternarniy
print(f'max={max}')

day_of_week=int(input("Input number day of week: "))
if day_of_week>=1 and day_of_week<=5:  #[1;5]      1<=day_of_week<=5
    print("working day")
elif day_of_week==6 or day_of_week==7:
    print("weekend")
else:
    print("Error")

# # # match
match day_of_week:
    # pattern1
    case 1:
        print("working day")
    case 2|3|4|5:
        print("working day")
    # pattern2
    case 6|7:
        print("weekend")
    # default pattern
    case _: #alternativ varaiable
        print("Error")

step1="Вмокнув пензлика в банку з фарбою"
step2="Провів вгору і вниз пензликом"
step3="Пересунув банку з фарбою вправо"
step4="Зробив крок вправо"

# import random
# # shtaheta_break=random.randint(1,10)

# # elemenets=10 #штахети
# # count=1
# # while count<=elemenets:
# #     print("="*10,count,"="*10)
# #     if count==3 or count==7:
# #         print("Я змахлював... не пофарбував штахету №", count)
# #         count+=1
# #         continue
# #     if count==shtaheta_break:
# #         print("Я пішов на перерву...")
# #         break
# #     print(step1)
# #     print(step2)
# #     print(step3)
# #     count=count+1
# #     print(step4+" до штахети №", count)
# # else:
# #     print(f"Stop!!! А штахети №{count} нема!")

# # print(f"Було пофарбовано {count-1} штахет")




# # # # """
# # # # for змінна in послідовність:
# # # #     команди
# # # # """

# # # # """
# # # # for змінна in послідовність:
# # # #     команди
# # # # else:                     
# # # #     команди
# # # # """

# # # # # range(10) => [0,1,2,...,9]
# # print(list(range(1,11)))
# shtaheta_break=random.randint(1,11)

elemenets=10 #штахети
for count in range(1,elemenets+1):  #1,2,3,4,5,6,7,8,9,10
    print("="*10,count,"="*10)
    if count==3 or count==7:
        print("Я змахлював... не пофарбував штахету №", count)
        continue
    if count==5:
        print("Я пішов на перерву...")
        break
    print(step1)
    print(step2)
    print(step3)
    print(step4+" до штахети №", count+1)
else:
    print(f"Stop!!! А штахети №{count+1} нема!")

print(f"Було пофарбовано {count-1} штахет")


suma=0 #0+1+...+9
print(type(suma))
for i in range(10):
    suma+=i
    print(i,end="\t")

print("\n",suma)

# suma=0 #0+1+2+...+10
# print(type(suma))
# for i in range(11): #range(1,11,1)
#     suma+=i
#     print(i,end="\t")

# print("\n",suma)

# print(list(range(4,10,2))) #[4, 6, 8]

# # """
# # while умова(предикат):
# #     команди (ітерації)
# # else:
# #     команди (успішний цикл без break)
# # """
# #Знайти суму 1,2,3, ..., 10
# suma=0 
# i=1
# while i<11:
#     suma=suma+i
#     print(i,end="\t")
#     i+=1
# else:
#     print("\nGood finish!")

# print(f"\nsuma={suma}")

# #Знайти суму 1,2,3, ..., 10
# suma=0 
# i=1
# while True:
#     if i>10:
#         break
#     suma=suma+i
#     print(i,end="\t")
#     i+=1
# else:
#     print("Good finish!") # never working


# print(f"\nsuma={suma}")

# # """
# # 1. Вмочив пензлик у фарбу 
# # 2. Пофарбував штахету #i
# # 3. Крок вправо на одну штахету
# # ... допоки не закінчаться штахети в паркані
# # паркан складається з 20 штахет
# # """

# # for item in range(20):
# #     if item==10: 
# #         print("Break.....")
# #         break
# #     working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(item+1)
# #     print(working)
# # else:
# #     print("Work done!!!") #not break cicle

# # # Том Соєр вирішив фарбувати кожну другу штахету
# # for item in range(20): #0,1,2,3..,19
# #     if item%2==1: 
# #         print("Continue item #",item+1)
# #         continue
# #     if item==10: 
# #         print("Break.....")
# #         break
# #     working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(item+1)
# #     print(working)
# # else:
# #     print("Work done!!!") #not break cicle

# # for item in range(1,21): #1,2,3..,20
# #     if item%2==1: 
# #         print("Continue item #",item)
# #         continue
# #     if item==10: 
# #         print("Break.....")
# #         break
# #     working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(item)
# #     print(working)
# # else:
# #     print("Work done!!!") #not break cicle


# # # break continue
# # # while
# # print("Working with while...")
# # cout_shtaheta=20
# # all_shtahet=20
# # while cout_shtaheta<all_shtahet:
# #     cout_shtaheta+=1 
# #     # cout_shtaheta=cout_shtaheta+1
# #     working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(cout_shtaheta+1)
# #     print(working)
# # else:
# #     print("Work done!!!") #not break cicle