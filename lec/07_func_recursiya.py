# # def namef(p1,p2...): #заголовок функції => сигнатура
# #     pass    # тіло функції : return

# 6!=1*2*3*4*5*6
# 1!=1 

# fact=1
# n=6
# for i in range(n,1,-1):  #6,5,4,3,2,1
#     fact=fact*i  #6,6*5,30*4,120*3,360*2

# print("fact=",fact)
# # =======================================
def factorial(n):
    if n==1: # 1)умова зупинки рекрсії
        return 1
    else:
        return n*factorial(n-1)  #виклик рекрсії самої себе
# #глибина рекурсії => 1000   > RecursionError
n=6

result_fact=factorial(n)
print("result_fact=",result_fact)

# # Напишіть функцію, яка приймає число і виводить відповідну
# # кількість вкладених пар круглих дужок. Наприклад: число 4 – (((())))
# # 1 "()"  2 =>"("+"()"+")"  3 => "("+"("+"()"+")"+")"

def evenD(n):
    if (n==1):
        return "()"
    else:
        return "("+evenD(n-1)+")"

print(evenD(2))
# print(evenD(3))
# # 2=>   evenD(2)=>  "("+evenD(1)+")" => "()"
# #          "(())" <=  "("+"()"+")"   <=


# # 3=>   evenD(3)=>  "("+evenD(2)+")" =>"("+ "("+evenD(1)+")"+")" => "()"
# #      "((()))" <=   "("+"(())"+")" <= "("+"("+"()"+")"+")"   <=



def factorialInv(m,n):
    if m==n:
        return n
    else:
        return m*factorialInv(m+1,n)

# print(factorialInv(1,3))
# # 3=>   factorialInv(1,3)=>  1*factorialInv(2,3) =>1*(2*factorialInv(3,3))) => 1*(2*(return 3 stop ))
# #                   6    <=     1*6              <= 1*(6)                   <=



# lambda parameters : eval

qvadr=lambda x : x**2
print(qvadr(3))

print(qvadr(2)+qvadr(3))

print_info=lambda : print("info for me!!!")
print_info()
print_info()
print_info()
# # OR======================== без імені=====
(lambda : print("info for me!!!"))()


result=10+(lambda x,y : x**2+y**3)(2,3)
print(type((lambda x,y : x**2+y**3)))
print(result)
f1=lambda x,y : x**2+y**3
result1=10+f1(2,3)
print(result1)

# # #================ filter() , map()
def is_div_3_and_5(number):
    if number%3 == 0 and number%5==0:
        return True
    return False

list1=[1,6,3,7,5,9,15,30]
# print(filter())
new_list=list(filter(lambda x: x%3==0,list1))

new_list1=[x for x in list1 if x%3==0]
print(new_list)
print(new_list1)
new_list2_filter=filter(is_div_3_and_5,list1)
# print(list(new_list2_filter))
print(list(range(10)))

def cube(n):
    return n**3

new_list2=list(map(lambda x: x**2, list1))
print(new_list2)
new_list3=list(map(cube, list1))
print(new_list3)