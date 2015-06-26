#!/usr/bin/python
#Simple SMTP Mail Sender
#I am tested with google mail - content_type starttls
#@author Fatih USTA
#@date 2013/11/10
#fatihusta.com


import smtplib


recipients = 'recipient@example.com'

auth_addr = 'example@gmail.com'
password = 'yOurPassW0rD'
account_name = 'Optional Account Name'
smtp_address = 'smtp.googlemail.com'
smtp_port = '587'

signature = """
<br>
<br>
---<br>
<b>Fatih USTA<b>
"""

subject = 'Mail subject'

message = """
Test Message<br>
<br>
"""

#HTML Body
#message = """
#<b>This is HTML message.</b>
#<h1>This is headline.</h1>
#"""

from_addr = account_name + '<' + auth_addr + '>'
mime_version = 'MIME-Version: 1.0'
content_type = 'Content-type: text/html'

smtpserver = smtplib.SMTP(smtp_address, smtp_port)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(auth_addr, password)

header = 'From: ' + from_addr + '\n' + 'To: ' + recipients + '\n' + mime_version + '\n' + content_type + '\n' + 'Subject: ' + subject + '\n'
#print  'From: ' + from_addr + '\n' + 'To: ' + recipients + '\n' + 'Subject: ' + subject + '\n\n' + message + '\n' + signature + '\n\n'

mail = header + '\n' + message + '\n\n' + signature + '\n\n'
print 'Sending Mail...' + '\n'

smtpserver.sendmail(from_addr, recipients, mail)
print 'done!'

smtpserver.close()
