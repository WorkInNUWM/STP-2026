import os
# csv =>  "\t"   " "   ","  "."  ";"  ","  "|"
# dict_for_json = { "username": "TSShrol", "email": "shrolts@gmail.com"}
# json = > is string => "{ "username": "TSShrol", "email": "shrolts@gmail.com"}"


import csv
students=[
   ['Фінчук', 'Віталій'],
    [ 'Генеральчук','Микола'],
    ['Дзюбак','Вікторія' ],
    ['Шпес','Олександра' ],
    ['Chovpylo','Ivan' ],
    ['Дяк','Богдан' ],
    ['Стельмах','Світлана' ],
    ['Шманін','Михайло' ],
    ['Гнатюк','Олександр']
]

print(os.getcwd()) #E:\Tetiana\CT_I_Python_2_2024
path_file_to_csv=os.path.join(os.getcwd(),"12_files_csv_json","students.csv")
print(path_file_to_csv) #E:\Tetiana\CT_I_Python_2_2024\12_files_csv_json\students.csv
#запис
with open(path_file_to_csv,'wt') as file_record:
    recordcsv=csv.writer(file_record, delimiter=";",lineterminator="\n")
    recordcsv.writerows(students)

# читання
with open(path_file_to_csv,'rt') as file_read:
    readercsv=csv.reader(file_read, delimiter=";")
    print(readercsv)
    # for student in readercsv:
    #     print(student)
    students=[studetn for studetn in readercsv]
    print(students)

# #task1

text="""
author, canvas
Vincent Willem van Gogh, "Vase with sunflowers"
Rembrandt Harmenszoon van Rijn, "Aristotle"
Leonardo da Vinci, "Self-portrait
"""

# перетворення в список 
text_for_row=text.split("\n")
print(text_for_row)
text_for_row_csv=[item.split(",") for item in text_for_row if len(item)>0]
print(text_for_row_csv)

# # OR:
# text_for_row_csv=[]
# for item in text_for_row:
#     if len(item)>0:
#         text_for_row_csv.append(item.split(","))
# print(text_for_row_csv)

author_canvas=[
["author", "canvas"],
["Vincent Willem van Gogh", "Vase with sunflowers"],
["Rembrandt Harmenszoon van Rijn", "Aristotle"],
["Leonardo da Vinci", "Self-portrait"]
]
# # "," - one ceil ,   ";" - many ceils
path_file_to_csv1=os.path.join(os.getcwd(),"12_files_csv_json","painters.csv")
with open(path_file_to_csv1,"wt") as file_for_record:
    csv.writer(file_for_record,delimiter=";",lineterminator="\n").writerows(author_canvas)

# print("*"*30)
# task2
with open(path_file_to_csv1,"rt") as file_for_read:
    result=csv.DictReader(file_for_read,delimiter=";",fieldnames=["author","canva"])
    #get header fieldnames from DictReader and store in list
    headers = result.fieldnames
    # print(headers)
    author_of_canvas=[]
    for item in result:
        # print(item)
        author_of_canvas.append(item)
    author_of_canvas=author_of_canvas[1:]
    print(author_of_canvas)




#task3
# imdb.csv
imdb = [
    {
        'title': 'Lord of the Rings: Two towers',
        'year': 2002,
        'rating': 8.7},
    {
        'title': 'Matrix',
        'year': 1999,
        'rating': 8.7},
    {
        'title': 'Interstellar',
        'year': 2014,
        'rating': 8.5},
    {
        'title': 'Back to the Future',
        'year': 1985,
        'rating': 8.5},
    {
        'title': 'Logan: Wolverine',
        'year': 2017,
        'rating': 8.1}
]


with open(os.path.join(os.getcwd(),"12_files_csv_json","imdb.csv"),"wt") as file_for_write:
    recordcsv=csv.DictWriter(file_for_write,delimiter=";",fieldnames=["title","year","rating"],lineterminator="\n")
    recordcsv.writeheader()
    recordcsv.writerows(imdb)

print("*"*40)
# print(f"{str(os.getcwd())}\\12_files_csv_json\\imdb.csv");
with open(f"{str(os.getcwd())}\\12_files_csv_json\\imdb.csv","rt") as file_for_read:
    writecsv=csv.DictReader(file_for_read,delimiter=";",fieldnames=["title","year","rating"],lineterminator="\n")
    list_movies=[]
    for row in writecsv:
        print(row)
        list_movies.append(row)
    print(list_movies[1:])


print(os.getcwd())