import os
import time
from datetime import datetime
import mysql.connector
# from dotenv import load_dotenv
from database import make_table, get_connection
#
# load_dotenv()
# # folder = input("Enter the path to the folder you want to scan: ")
# # folder = r"C:\Users\jelle\OneDrive - Hogeschool Leiden\ifiift"
#
#
#
# def main(path_input):
#     folder = path_input
#     mydb = get_connection()
#     mycursor = mydb.cursor()
#
#     make_table(mydb)
#
#     for root, dirs, files in os.walk(folder):
#         ti_c = os.path.getctime(root)
#         if len(files) > 0 and files != ["0"] and "." in files[0]:
#             for file in files:
#                 if "_" not in file:
#                     path = r"\\?\\" + os.path.join(root, file)
#                     size = os.stat(path).st_size
#                     print(f"{file}, {size} bytes")
#                     c_ti = datetime.strptime(time.ctime(ti_c), "%a %b %d %H:%M:%S %Y").isoformat()
#                     # print(c_ti)
#                     # print(type(size))
#
#                     sql = "INSERT INTO file_info (path, file_name, file_size, created_time) VALUES (%s, %s, %s, %s)"
#                     val = (root, file, size, c_ti)
#                     mycursor.execute(sql, val)
#
#     mydb.commit()



from file_scanner import main as scan_folder
import os
from filters import get_arguments
import time
from datetime import datetime
import mysql.connector
from dotenv import load_dotenv
from database import make_table, get_connection

args = get_arguments()
folder = args.folder


if os.path.exists(folder) == True:
    scan_folder(folder)
else:
    print("Path does not exits!")

print("File scanner completed")

