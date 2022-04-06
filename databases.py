

import sqlite3

conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fileName TEXT)')
    conn.commit()

fileList_tuple = ('information.docx', 'Hello.txt', 'myImage.png', \
                  'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')

for x in fileList_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO tbl_files (col_fileName) VALUES (?)', (x,))
            print(x)
conn.close()








