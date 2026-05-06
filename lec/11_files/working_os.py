import os


info_methods="""
OS routines for NT or Posix depending on what system we're on.

This exports:
  * all functions from posix or nt, e.g. unlink, stat, etc.
  * os.path is either posixpath or ntpath
  * os.name is either 'posix' or 'nt'
  * os.curdir is a string representing the current directory (always '.')
  * os.pardir is a string representing the parent directory (always '..')
  * os.sep is the (or a most common) pathname separator ('/' or '\')
  * os.extsep is the extension separator (always '.')
  * os.altsep is the alternate pathname separator (None or '/')
  * os.pathsep is the component separator used in $PATH etc
  * os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
  * os.defpath is the default search path for executables
  * os.devnull is the file path of the null device ('/dev/null', etc.)
"""

# with вираз as зміна
with open('methods_os.txt','w') as fileos:
    fileos.write(info_methods)

print(os.getcwd()) # E:\Tetiana\CT_I_Python_2_2024
print(os.path.realpath('.')) #  E:\Tetiana\CT_I_Python_2_2024
# list catalog
print(os.listdir())

# зміна каталогу
os.chdir("11_files")
# виведення шляху до  поточного каталоуг 
print(os.path.abspath('.')) #  E:\Tetiana\CT_I_Python_2_2024\11_files
# створення нового каталогу
if not os.path.exists('test_dir'):
    os.mkdir('test_dir')

# list catalog
print(os.listdir())
# перейменувати каталогу або файлу
try:
    os.rename('test_dir','new_test_dir')
except FileExistsError as ex:
    print(ex)

import shutil
# скопіювати файл methods_os into 
path_to=os.path.join(os.path.abspath("."),'test_dir') #11_files
print(path_to)
# using relative path
# path_to_file=os.path.relpath(os.path.abspath("."),'methods_os.txt') 
# path_file_for_copy=os.path.join(path_to_file,'methods_os.txt') #

# using absolute
path_file_for_copy=os.path.abspath("E:\\Tetiana\\CT_I_Python_2_2024\\"+'methods_os.txt')
print(path_file_for_copy)
shutil.copy(path_file_for_copy,path_to)
# print(os.path.relpath(os.path.abspath("."),'methods_os.txt'))
# E:\Tetiana\CT_I_Python_2_2024\methods_os.txt
# methods_os.txt
# deleting ditectory new_test_dir to test_dir

# os.chdir("test_dir")
# print(os.getcwd())
# os.remove("methods_os.txt")

# де ми?
print(os.getcwd())
absolute_path_to_file=os.path.join(os.getcwd(),"test_dir","methods_os.txt")
print(absolute_path_to_file)
if os.path.exists(absolute_path_to_file):
    os.remove(absolute_path_to_file)

path_to_dir_for_deleting=os.path.join(os.getcwd(),"new_test_dir")
if os.path.isdir(path_to_dir_for_deleting):
    os.rmdir(path_to_dir_for_deleting)


import glob
# пошук файлів в поточному каталоці => 11_files
list_files=glob.glob("[sr]*")
print(list_files)

list_files=glob.glob("*[! x].*")
print(list_files)

# os.chdir("..") # перехід на рівень в дереві каталогів вгору
# print(os.getcwd())
# os.chdir("..") # перехід на рівень в дереві каталогів вгору
# print(os.getcwd())

# os.chdir("..") # перехід на рівень в дереві каталогів вгору
# print(os.getcwd())