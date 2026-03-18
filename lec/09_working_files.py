# ================records (write) in file====
# Mode files XY
# X:
# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	create a new file and open it for writing
# 'a'	open for writing, appending to the end of the file if it exists
# Y:
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)
filewr=None
try:
    filewr=open("test_file.txt","wt",encoding="utf-8")
    # variant 1
    # print("Test records in file", file=filewr)
    # print("Тестування запису у файл через print", file=filewr )
    # variant 2
    res=filewr.write("Тестування запису у файл через метод write")
    # filewr.close()
except FileNotFoundError as ex:
    print("Не знайдно файл",ex)
except Exception as ex:
    print(ex)
    filewr.close()
else:
    filewr.close()

# ==================append and  write to file===
import os
file_append=""
# absolute path: E:\Tetiana\NUWM_2025\ICT-31_Python\dir_files\test_file.txt
# relative path: dir_files\test_file.txt
dir_path="E:\\Tetiana\\NUWM_2025\\ICT-31_Python\\dir_files"

file_append=os.path.join(dir_path,"test_file.txt")
print(file_append)
print(os.path.exists(file_append))
if os.path.exists(file_append):
    os.rename(file_append,os.path.join(dir_path,"text_rile_rename.txt"))
else:
    print("ERROR!!")

print(os.path.curdir)
cur_dir=os.path.curdir

working_dir=os.path.join(cur_dir,"dir_files")
path_file=os.path.join(working_dir,"text_fIle1.dat")
# менеджер контексту з файлом
with open(path_file,"wt",encoding="utf-8") as file_wr2:
    rez=file_wr2.write("test write with 'with'\n")
    print(rez)

with open(path_file,"at",encoding="utf-8") as file_wr2:
    rez=file_wr2.write("append text ro end test write with 'with'")
    print(rez) #кількість записаних символів


# зчитування read, readln, readlines
with open(path_file,"rt",encoding="utf-8") as file_r2:
    rez_text=file_r2.read()
    print(rez_text)

# read+fragment
with open(path_file,"rt",encoding="utf-8") as file_r:
    text=""
    count_symbol=10
    while True:
        fragment=file_r.read(count_symbol)
        if not fragment:
            break
        text+=fragment
        print(fragment)
        print(len(fragment))

print("text=",text)

# readline
with open(path_file,"rt",encoding="utf-8") as file_r:
    text=""
    line=file_r.readline()
    while line:
        text+=line
        line=file_r.readline()
        
print("text=",text)


# readlines
with open(path_file,"rt",encoding="utf-8") as file_r:
    list_lines=file_r.readlines()
    print(list_lines)
    text="".join(list_lines)
        
print(f'text="{text}"')



# ================binary==================
# 
bindata=bytes(range(16,125))
print(bindata) 
bindata_alpha=bytes(range(65,126))
print(bindata_alpha)
path_filebinary=os.path.join(dir_path,"binary.dat")

with open(path_filebinary,"wb") as file_wb:
    file_wb.write(bindata_alpha)
    text="""
# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	create a new file and open it for writing
# 'a'	open for writing, appending to the end of the file if it exists
тест кодування
    """
    # file_wb.write(bytes(text, encoding="UTF-16"))




with open("C:\\Users\\Tetiana\\Pictures\\Зображення1.png","rb") as file_rb:
    print(file_rb.read())


# tell => where currsor, seek => step ,

with open(path_filebinary,"rb") as file_rb:
    print(file_rb.tell())
    # print(file_rb.seek(-29,2)) # зміщення з остнньої позиції вправо на b'abcdefghijklmnopqrstuvwxyz{|}'
    # print(file_rb.seek(26,0)) # зміщення з першої позиції вправо на b'abcdefghijklmnopqrstuvwxyz{|}'
    # print(file_rb.tell())
    print(file_rb.seek(8,0)) # зміщення з першої позиції вправо на b'abcdefghijklmnopqrstuvwxyz{|}'
    print(file_rb.tell())
    print(file_rb.seek(8,1)) # зміщення з першої позиції вправо на b'abcdefghijklmnopqrstuvwxyz{|}'
    print(file_rb.tell())
    print(file_rb.read())