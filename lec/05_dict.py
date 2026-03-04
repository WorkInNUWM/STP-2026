#{key1:value1, key2:value2,...,keyN:valueN}
library={
    "Шевченко":["Катерина","Кобзар","Заповіт"],
    "Франко":["Каменярі","Фарбований лис"]
}
print(library)
print(library["Шевченко"])
print(library["Франко"])
print(library["Шевченко"][1])
print(library.get("Шевченко")[1])

print(library.keys())
print("*"*30)
for author in library.keys():# iter
    print("author=",author)
    # print(library[author])
    count=1
    for book in library[author]:
        print(f"\t{count}.{book}")
        count+=1

print("*"*30)
for books in library.values(): 
    print("books:",books)

print(list(library.items()))
# # added new elemets in dict:
library["Леся Українка"]=["Лісова пісня","Contra Spem..."]
# # library["Леся Українка"]="Лісова пісня"

print("*"*30)
for author, books in library.items(): #(key, value)
    print(f"Author {author} wroten:")
    count=1
    for book in books:
        print(f"\t{count}. {book}")
        count+=1

groups=["ICT-31", "CT-21"]
count_students=[22,20]
print(list(zip(groups,count_students)))
print(tuple(zip(groups,count_students)))
print(dict(zip(groups,count_students)))
print(dict([(x, x*x) for x in range(1,21)]))

# print("*"*30)
# key_lib=iter(library)
# print(key_lib)
# # print(key_lib.__next__)

# print(next(key_lib))
# print(next(key_lib))
# print(next(key_lib))
# # print(next(key_lib)) # Exception

# # groups=library.fromkeys("Python")
# # print(groups)
# library.setdefault("Сосюра",[])
# print(library["Сосюра"])
# del library["Леся Українка"]
# print(library)