import os
import mysql.connector
from dotenv import load_dotenv
import argparse

load_dotenv()
parser = argparse.ArgumentParser()

def get_connection():
    return mysql.connector.connect(
        host = os.getenv("host"),
        user = os.getenv("user"),
        password = os.getenv("password"),
        database = os.getenv("database")
    )
mydb = get_connection()
mycursor = mydb.cursor()

#get specific filetypes
mycursor.execute("SELECT DISTINCT extension from file_info")
unique = [row[0] for row in mycursor.fetchall()]
parser.add_argument("--filetype", help="Search for 1 or more specific file types", choices=unique, nargs="*", type=str)
args = parser.parse_args()


filetypes = args.filetype
