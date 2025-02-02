import os
import time
from datetime import datetime
import mysql.connector
from dotenv import load_dotenv
from database import make_table, get_connection

load_dotenv()
# folder = input("Enter the path to the folder you want to scan: ")
# folder = r"C:\Users\jelle\OneDrive - Hogeschool Leiden\ifiift"



def main(path_input):
    folder = path_input
    mydb = get_connection()
    mycursor = mydb.cursor()

    make_table(mydb)

    for root, dirs, files in os.walk(folder):
        ti_c = os.path.getctime(root)
        if len(files) > 0 and files != ["0"] and "." in files[0]:
            for file in files:
                if "_" not in file:
                    path = r"\\?\\" + os.path.join(root, file)
                    size = os.stat(path).st_size
                    extension = file.split(".")
                    print(f"{file}, {size} bytes, {extension[-1]}")
                    c_ti = datetime.strptime(time.ctime(ti_c), "%a %b %d %H:%M:%S %Y").isoformat()
                    # print(c_ti)
                    # print(type(size))

                    sql = "INSERT INTO file_info (path, file_name, file_size, created_time, extension) VALUES (%s, %s, %s, %s, %s)"
                    val = (root, file, size, c_ti, extension[-1])
                    mycursor.execute(sql, val)

    sql = "SELECT * FROM file_info WHERE file_size = 9468675"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for row in result:
        print(result)
    # print()
    mydb.commit()