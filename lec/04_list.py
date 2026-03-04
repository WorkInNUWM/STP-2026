# # #list -списки
digits1=[0,1.3,2,"3",4,5,6,7,8,9]
print(digits1)
digits=[0,1,2,3,4,5,6,7,8,9]
print(digits)
print(type(digits))
print(id(digits))


list1=[23,"Python",'a',45.5]
# #     0     1     2   3 
print(f'2-й елемент списку {list1} => {list1[1]}')

list2=[] # => []
list21=[]
# # #сформувати список чисел, що є квадратами чисел від 1 до 10
for item in range(1,11):
    list2.append(item**2)
    list21.append(item)

print("list21=",list21,sep="")    
print("list2=",list2,sep="")    

# # скорочений синтаксис або синтакси включенням  заповнення елементів списку
list2_v2=[item**2 for item in range(1,11)]
print("list2_v2=",list2_v2)    

# # #random
import random

list3=list()  # =>[]
print(list2,"\n",list3)


print(range(0,11,2))
list_generate_numbers=list(range(0,11,2))
print(list_generate_numbers)
list_symbols=list("We are learning Python!")
print(list_symbols)
# list_words="We are learning Python!".split(sep=" ") # ==
list_words="We are learning Python!".split()        # ==
print(list_words)

# # #create list with number where number%3==0 and number%7==0 by [1,100]

list_div_3_and_7=[value for value in range(1,101) if value%3==0  and value%7==0]
print(list_div_3_and_7)

# # #using methods and function to list
list_random=[]
print(f"id{list_random}={id(list_random)}")
for _ in range(10):
#     # randint(a,b) => Return random integer in range [a, b], including both end points.
    list_random.append(random.randint(1,100))

print("list_random=",list_random)

list_random[2]=333
print("chanhed list_random=",list_random)
print(f"id{list_random}={id(list_random)}")

list_random[0:5:2]=[333,333,333]
print("chanhed list_random=",list_random)
print(f"id{list_random}={id(list_random)}")

list_random.append(555)
print("chanhed list_random=",list_random)
print(f"id{list_random}={id(list_random)}")

# # #insert 55 in index 4
list_random.insert(4,55)
print("insert 55 in list: ",list_random)
# #return index number 55 from list_random
print("index number 55 => ", list_random.index(55))
# # #remove 55
list_random.remove(55)
print("remove 55 from list: ",list_random)

# # #delete last element of list
print("list before delete: ",list_random)
list_random.pop()
print("list after delete last element => ", list_random)

# # # take last elemnts of list
element=list_random.pop()
print("last elements of list",element)

print("*"*30,"\nlist before reverse: ",list_random)
list_random.reverse()
print("reverse with method =>",list_random)
print("reverse with slice =>",list_random[::-1])
list_random.sort()
print("sort=>",list_random)
list_random.sort(reverse=True)
print("sort reverse=>",list_random)
print("len=>",len(list_random) )
print("min=>",min(list_random) )
print("max=>",max(list_random) )
print("sorted=>",sorted(list_random))

# ##!!! copy deepcopy
list_first=[2,3,76,32,42]
list_second=list_first
list_third=list_first.copy()
# # OR
# # list_third=list_first[:]
print(f"list_first=>{list_first} ; id(list_first)=>{id(list_first)}")
print(f"list_second=>{list_second} ; id(list_second)=>{id(list_second)}")
print(f"list_third=>{list_third} ; id(list_third)=>{id(list_third)}")

list_first[4]=444
print("After change element in list:")
print(f"list_first=>{list_first} ; id(list_first)=>{id(list_first)}")
print(f"list_second=>{list_second} ; id(list_second)=>{id(list_second)}")
print(f"list_third=>{list_third} ; id(list_third)=>{id(list_third)}")


list_third[0]=[11,22,33]
print("After change element in list_third:")
print(f"list_third=>{list_third} ; id(list_third)=>{id(list_third)}")
print("*"*30)

list4=list_third.copy() #неглибоке копіювання

import copy
list5=copy.deepcopy(list_third) #глибоке копіювання

print(f"list_third=> {list_third}")
print(f"list4=> {list4}")
print(f"list5=> {list5}")

## list_third[0]=111
## list4[0]=1111
## print("After changed list_thrid[0]:")
## print(f"list_third=> {list_third}")
## print(f"list4=> {list4}")
## print(f"list5=> {list5}")

print(id(list_third[0]),id(list_third[0][1]))
print(id(list4[0]),id(list4[0][1]))
print(id(list5[0]),id(list5[0][1]))
list_third[0][1]=222
print("After changed list_thrid[0]:")
print(f"list_third=> {list_third}")
print(f"list4=> {list4}")
print(f"list5=> {list5}")


# #1 2 3 
# #4 5 6
# #7 8 9

matrix_3x3=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(matrix_3x3)
print(matrix_3x3[1][2])

# # suma
suma=0
n_row=len(matrix_3x3)
for i in range(n_row):
    # print(matrix_3x3[i])
    n_col=len(matrix_3x3[i])
    for j in range(n_col):
        suma+=matrix_3x3[i][j]
        print(matrix_3x3[i][j], end=" ")
    print()

print("suma=",suma)
print("*"*50)
for row in matrix_3x3:
    print(row)
    n_col=len(matrix_3x3[i])
    for col in row:
        suma+=col
        print(col, end=" ")
    print()

print("suma=",suma)