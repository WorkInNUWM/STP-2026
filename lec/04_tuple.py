tuple1=() # => ()
tuple2=tuple() # => ()
print(id(tuple1))
print(id(tuple2))

tuple3=("admin","Qwerty-1","email@at.ua")
print(tuple3)

# # tuple3[0]="superadmin" #TypeError
# # print(tuple3)
print(tuple3[0])
user_login,password,email=tuple3
print(user_login,password)

tuple4=(333,)
print(type(tuple4),tuple4)

tuple5=tuple([333])
print(type(tuple5),tuple5)


tuple6=777,
print(type(tuple6), tuple6)

list_seasons=["summer","fall","winter","spring"]
tuple7=list(enumerate(list_seasons))
print(tuple7)

x,y,z=34,67.4,4444
print(x,y,z)

krainy = (
    ("Ukrain", 52.3, ("Rivne", 30000), ("Kiev", 50000)),
    ("Poland", 34.3, ("Lublin", 30000), ("Varshava", 50000))
)
for nazva, plosha, misto1, stolyca in krainy:
    # nazva, plosha, misto1, stolyca = kraina
    print("\nКраїна: {} площа: {} км^2".format(nazva, plosha))
    print("місто %s з кількістю населення %d осіб" % (misto1[0], misto1[1]))
    print("столиця %s з кількістю населення %d осіб" % (stolyca[0], stolyca[1]))