import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
folder = r"C:\Users\jelle\OneDrive - Hogeschool Leiden\ifiift"

mydb = mysql.connector.connect(
    host = os.getenv("host"),
    user = os.getenv("user"),
    password = os.getenv("password"),
    database = os.getenv("database")
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS file_scanner")
mycursor.execute("DROP TABLE IF EXISTS file_info")
mycursor.execute("CREATE TABLE IF NOT EXISTS file_info (id INT AUTO_INCREMENT PRIMARY KEY, path VARCHAR(255), file_name VARCHAR(255))")


for root, dirs, files in os.walk(folder):
    if len(files) > 0 and files != ["0"] and "." in files[0]:
        for file in files:
            if "_" not in file:
                print(file)

                sql = "INSERT INTO file_info (path, file_name) VALUES (%s, %s)"
                val = (root, file)
                mycursor.execute(sql, val)

mydb.commit()