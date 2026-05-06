import shelve
import os
# ==========record (write) in file
# filewr=None
# try:
#     # dir_path="E:\\Tetiana\\NUWM_2025_2026\\STP\\lec\\11_files\\"
#     # file_path="record.txt"
#     dir_path=os.path.join("lec","11_files")
#     print(dir_path)
#     # print(os.path.dirname("record.txt"))
#     file_path=os.path.join(dir_path,"record.txt")
#     print(file_path)

#     filewr=open(file_path,"wt",encoding="utf-8")
#     text="""
#     Mode files   ХY :
#     X:
#     r - читання
#     w - запис в існуючий файл, або створення нового
#     x - запис у файл, якщо файл не існує
#     a - додавання в кінець файлу

#     Y:
#     t - файл текстовий (за замовчуванням)
#     b - файл бінарний
#     """
#     # raise Exception("Checking Exception")
#     res=filewr.write(text)
#     print(res)
# except FileNotFoundError as ex:
#     print("Error=>", ex)
# except Exception as ex:
#     print("We are closed file")
#     # filewr.close()
# else:
#     print("Not exception")
#     print("Count record bytes=>", res)
#     # filewr.close()
# finally:
#     if filewr !=None:
#         filewr.close()
#     print("close file")



# # # ======================= append and write from file 
# file_append=""
# # # E:\Tetiana\NUWM_2025_2026\STP\lec\11_files\working_files.py
# # # lec\11_files => relative path відносний щодо інтерпретатора Python
# # # E:\Tetiana\NUWM_2025_2026\STP\lec\11_files\record.txt  => absolute path
# try:
#     # file_append=open('lec/11_files/record.txt','at')
#     file_append=open('lec/11_files/record.txt','xt')
#     print(f'type=> {type(file_append)}')
#     text="""Write to an Existing File
#     To write to an existing file, you must add a parameter to the open() function:
#     "a" - Append - will append to the end of the file
#     "w" - Write -will overwrite any existing content"""
#     print(text+"\n", file=file_append)
#     file_append.write(text+"\n")
# except FileExistsError:
#     print("record.txt already exists!")
# else:
#     file_append.close()


# # # #====================== read, readline(), readlines()
# file_r=open("lec/11_files/record.txt","rt",encoding="utf-8")
# # # text=file_r.read()
# # # text=file_r.readlines()
# # # text=file_r.readline()
# text=""
# while True:
#     line=file_r.readline()
#     if not line:
#         break
#     text+=line

# words=text.split()
# print(words)
# file_r.close()
# print(text)
# print(len(text)) 


# #======================================
# file_r=open("lec\\11_files\\record.txt","rt",encoding="utf-8")
# count_symbol=100
# text1=''

# while True:
#     fragment=file_r.read(count_symbol)
#     if not fragment:
#         break
#     text1+=fragment
#     print(len(fragment))
#     print(fragment)

# # # print("row=",file_r.read())
# file_r.close()
# print(text1)
#
# print("*"*30)
# file_r=open("lec\\11_files\\record.txt","rt",encoding="utf-8")
# text2=""
# line=file_r.readline()
# while line:
#     text2 += line
#     line = file_r.readline()

# file_r.close()
# print(text2)

# #
# print("*"*50)
# text3=""
# file_r=open("lec\\11_files\\record.txt","rt")
# for line in file_r:
#     text3+=line

# file_r.close()
# print(text3)
# #
# #
# text4=""
# file_r=open("lec\\11_files\\record.txt","rt", encoding="utf-8")
# lines=file_r.readlines()
# print(lines)
# file_r.close()
# text5="".join(lines)
# print(text5)

# for line in lines:
#     text4+=line
# print(text4)
#
# # ===================binary files==========================
#
# \x89 => 10001001
bindata=bytes(range(0,256))
print(bindata)
bindata_alpha=bytes(range(65,126))
print(bindata_alpha)
file_b_w=open("lec\\11_files\\binary.dat","wb")
# file_b_w.write(bindata_alpha)
text="""Write to an Existing File
    To write to an existing file, you must add a parameter to the open() function:
    "a" - Append - will append to the end of the file
    "w" - Write - will overwrite any existing content
    проба"""
file_b_w.write(bytes(text,encoding="UTF-8"))
file_b_w.close()

#=====record by fragmnet=======
# file_b_w=open("lec\\11_files\\binary.dat","wb")
# len_data=len(bindata)
# setByte=0
# step=50
# while setByte<len_data:
#     rez=file_b_w.write(bindata[setByte:setByte+step]) #0:49 50:99... 
#     print(rez)
#     setByte+=step
# file_b_w.close()
#
print("==read=="*5)
file_b_r=open("lec\\11_files\\binary.dat","rb")
print(file_b_r.read())
file_b_r.close()
#

# print("====using tell()  and seek()")
# # # tell seek
# file_b_r=open("lec\\11_files\\binary.dat","rb")
# print(len(bindata_alpha))
# print(file_b_r.tell()) #
# print(file_b_r.seek(6)) # step moving => 90
# print(file_b_r.tell())

# # ## print(chr(97)) # when using bytes(range(0,266))
# print(file_b_r.seek(6,0))
# print(file_b_r.tell())
# print(file_b_r.seek(5,1))
# print(file_b_r.tell())
# print(file_b_r.seek(-10,2))
# print(file_b_r.tell())
# # # # print(chr(165))
# bdata=file_b_r.read()
# print(bdata)
# file_b_r.close()
#
# with open("lec\\11_files\\binary.dat","rb") as file_b_r:
#     # print(file_b_r.seek(32,0))
#     print(file_b_r.seek(-29,2))
#     # print(file_b_r.tell())
#     print(file_b_r.seek(4,1))
#     print(file_b_r.tell())
#     bdata=file_b_r.read()
#     print(bdata)
# #
with open("lec\\11_files\\binary.dat","rb") as fread:
    bytes_res=fread.read()
    print(bytes_res)
    convert_str=bytes_res.decode("UTF-8")
    print(convert_str)

# """
#    ['Python', 'Guido van Rossum'],
#     ['Scala', 'Martin Odersky'],
#     ['PHP', 'Rasmus Lerdorf'],
#     ['Ruby', 'Yukihiro Matsumoto'],
#     ['C', 'Dennis Ritchie'],
# """

filename = "lec\\11_files\\shelve_ex"
# working with files for dictonary
with shelve.open(filename, 'c') as shelve_wr:
    shelve_wr['Python'] = 'Guido van Rossum'
    shelve_wr['Scala'] = 'Martin Odersky'
    shelve_wr['C'] = 'Dennis Ritchie'

with shelve.open(filename, 'r') as shelve_r:
    key="Scala"
    if key in shelve_r:
        print(shelve_r[key])
    print(shelve_r['Python'])
    print(shelve_r['Scala'])

# with shelve.open(filename, 'r') as shelve_r:
#     value=shelve_r.get("C","None")
#     print(value)

# with shelve.open(filename, 'r') as shelve_r:
#     for key in shelve_r:
#         print(key," ",shelve_r[key])


# with shelve.open(filename, 'r') as shelve_r:
#     for avtor in shelve_r.values():
#         print(avtor)

# with shelve.open(filename, 'c') as shelve_wandr:
#     shelve_wandr["C"]="Ritchie"


# with shelve.open(filename, 'r') as shelve_r:
#     for avtor in shelve_r.values():
#         print(avtor)


# # os.mkdir("example1")
# # os.mkdir("E://Example1")
# # os.mkdir("E://Example1/exam")
# if os.path.exists("E://Example1/exam/f2.txt"):
#     os.rename("E://Example1/exam/f2.txt","E://Example1/exam/f1.txt")
# else:
#     print("ERROR")


# filename="E:/Example1/exam/f1.txt"
# with open(filename,'rt') as fileR:
#     rez=fileR.read()
#     # rez=fileR.readlines()

# print(rez)
# with open("listSt.txt",'wt') as fileW:
#     for row in rez:
#         print(row.rstrip("\n"))
#         listInfo=row.rstrip("\n").split()
#         print(listInfo)
#         if int(listInfo[1])>7:
#             listInfo[0]=listInfo[0].upper()
#         print(listInfo)
#         fileW.write(f"{listInfo[0]} {listInfo[1]} \n")

# print(rez)

