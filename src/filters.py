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
parser.add_argument("-ft", "--filetype", help="Search for 1 or more specific file types", choices=unique, nargs="*", type=str)
args = parser.parse_args()

# get filesize
mycursor.execute("SELECT DISTINCT file_size from file_info")
uniquesize = [row[0] for row in mycursor.fetchall()]
filetypes = args.filetype
parser.add_argument("-fs", "--filesize", help="Get all the file with a specific file type", choices=uniquesize, nargs=1, type=int)
args = parser.parse_args()

