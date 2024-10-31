#Project: Solo Email using Python3 on Linux Lab
#Purpose Details: Sends an email using python3 to my PSU account
#Course: IST 411
#Author: Joshua Gonzales
#Date Developed:10/15/2024
#Last Date Changed: 10/15/2024
#Rev:1

import getpass
import smtplib
from email.mime.text import MIMEText

fromAddress = "jjg6470@psu.edu"
toAddress = "jjg6470@psu.edu"
subject = "Test Email From Python3"
message = "Hello from python3, if you are seeing this the code works!!"
password = getpass.getpass(prompt="Enter Password: ")
email = MIMEText(message)
email['Subject'] = subject
email['From'] = fromAddress
email['To'] = toAddress

try:
	sendServer = smtplib.SMTP_SSL('authsmtp.psu.edu',465)
	sendServer.login(fromAddress, password)

	sendServer.sendmail(fromAddress, toAddress, email.as_string())
	print("Email Sent...")

except Exception as e:
	print(f"There has been an error: {e}")

finally:
	sendServer.quit()
