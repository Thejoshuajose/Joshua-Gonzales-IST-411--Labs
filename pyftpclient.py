# Project: Lab8 SFTP
# Purpose Details: Learning to use secure file transfer protocol
# Course: IST411
# Author: Joshua Gonzales
# Date Developed: 10/15/2024
# Last Date Changed: 10/15/2024
# Rev: 1

import pysftp
import getpass
import os

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

hostname = '172.29.135.40'
port = 1855
username = 'jjg6470'
password = getpass.getpass(prompt="Enter your password: ")

try:
    with pysftp.Connection(host=hostname, port=port, username=username, password=password, cnopts=cnopts) as sftp:
        print("Connection successfully established.")

        sftp.chdir('lab8/ftpsend/')
        print("FTPSEND Directory Files: ", sftp.listdir())

        local_file = 'JSONPayload.json'
        sftp.get(local_file)
        print("File has been found...")

        sftp.chdir('../ftpreceive/')
        sftp.put(local_file)
        print("File transferred to lab8/ftpreceive/ folder.")

        files = sftp.listdir()
        print("Files in lab8/ftpreceive/:", files)


        sftp.remove(local_file)
        print("JSONPayload.json removed from lab8/ftpreceive/ folder.")
        os.remove(local_file)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("SFTP transfer process completed.")
