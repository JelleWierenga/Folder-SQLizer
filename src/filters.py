import os
import mysql.connector
from dotenv import load_dotenv
import argparse
import datetime
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


parser = argparse.ArgumentParser(description="Search for files with specific filters.")


#get specific filetypes
parser.add_argument("-ft", "--filetype", help="Search for one or more specific file types", nargs="*", type=str)


# get filesize
parser.add_argument("--size", help="Filter files by specific file size (bytes)", type=int)


# get files with a specific name
parser.add_argument("--name", help="Filter files by exact file name", type=str)


# get files with created time
parser.add_argument("--modified", help="Filter files created at a given date (YYYY-MM-DD)", type=str)


args = parser.parse_args()