import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host = os.getenv("host"),
        user = os.getenv("user"),
        password = os.getenv("password"),
        database = os.getenv("database")
    )
# mydb = mysql.connector.connect(
#     host = os.getenv("host"),
#     user = os.getenv("user"),
#     password = os.getenv("password"),
#     database = os.getenv("database")
# )


def make_table(mydb):
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS file_scanner")
    mycursor.execute("DROP TABLE IF EXISTS file_info")
    mycursor.execute("CREATE TABLE IF NOT EXISTS file_info (id INT AUTO_INCREMENT PRIMARY KEY, path VARCHAR(255), file_name VARCHAR(255), file_size INT, created_time VARCHAR(255), extension VARCHAR(255))")