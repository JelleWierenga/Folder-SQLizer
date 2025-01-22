import os
import mysql.connector
from dotenv import load_dotenv
from database import make_table, get_connection

load_dotenv()
folder = r"C:\Users\jelle\OneDrive - Hogeschool Leiden\ifiift"


mydb = get_connection()
mycursor = mydb.cursor()

make_table(mydb)

for root, dirs, files in os.walk(folder):
    if len(files) > 0 and files != ["0"] and "." in files[0]:
        for file in files:
            if "_" not in file:
                path = r"\\?\\" + os.path.join(root, file)
                size = os.stat(path).st_size
                print(f"{file}, {size} bytes")
                # print(type(size))

                sql = "INSERT INTO file_info (path, file_name, file_size) VALUES (%s, %s, %s)"
                val = (root, file, size)
                mycursor.execute(sql, val)

mydb.commit()