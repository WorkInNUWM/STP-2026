import sqlite3
import os
#DML
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
my_file_db = os.path.join(BASE_DIR, 'techshop.db')
try:
    conn = sqlite3.connect(my_file_db)
    curs = conn.cursor()
    qt ='INSERT INTO computers VALUES(1, "PC", 5, 7570.50)'
    curs.execute(qt)
    curs.execute('INSERT INTO computers VALUES(2, "Notebook", 8, 11430.30)')
    conn.commit()
    curs.close()
    conn.close()
except Exception as ex:
    print(ex)


# # безпечний спосіб додавання даних - використовуючи заповнювач у вигляді ?:
conn = sqlite3.connect(my_file_db)
curs = conn.cursor()
curs.execute('INSERT INTO computers (id, name, count, price) VALUES(?, ?, ?, ?)', (3, 'NoteX', 7, 7970.20))
ins = 'INSERT INTO computers (id, name, count, price) VALUES(?, ?, ?, ?)'
curs.execute(ins, (4, 'Sumsung', 3, 11780.90))
conn.commit()
curs.close()
conn.close()
# #
#
conn = sqlite3.connect(my_file_db)
curs = conn.cursor()
curs.execute('INSERT INTO users (firstname, secondname, adress) VALUES ("Anna", "Vakula", "Rivne")')
curs.execute('INSERT INTO users (firstname, secondname, adress) VALUES ("Olga", "Ponomarenko", "Lviv")')
curs.execute("INSERT INTO orders (user_id, computers_id) VALUES(1, 2)")
curs.execute("INSERT INTO orders (user_id, computers_id) VALUES(2, 2)")
conn.commit()
curs.close()
conn.close()

#using executemany

list_product=[(6, 'NoteX', 7, 7970.20),
              (7, 'Sumsung', 3, 11780.90),
              (8, 'Note7X', 4, 9970.20)]
# безпечний спосіб додавання даних - використовуючи заповнювач у вигляді ?:
conn = sqlite3.connect(my_file_db)
curs = conn.cursor()
# curs.executemany('INSERT INTO сomputers (id, name, count, price) VALUES(?, ?, ?, ?)', list_product)
ins = 'INSERT INTO computers (id, name, count, price) VALUES(?, ?, ?, ?)'
curs.executemany(ins, list_product)
conn.commit()
curs.close()
conn.close()