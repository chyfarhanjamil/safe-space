
# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
  
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login("sieveoferat@gmail.com", "public()")
with open('email.txt') as f:
    lines = f.read().splitlines()
# message to be sent
message = "Someone violated social distancing"
recipients = lines
# sending the mail
s.sendmail("sieveoferat@gmail.com", recipients, message)
  
# terminating the session
s.quit()