import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'INSERT YOUR NAME'
email['to'] = 'INSERT MAIL ADDRESS(ES)'
email['subject'] = 'INSERT SUBJECT'

#Template example
email.set_content(html.substitute({'name': 'YOUR NAME', 'lastn': 'YOUR LASTNAME'}), 'html') # or use kwargs, e.g. name = 'x' , lastn = 'y'

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('YOUR GMAIL ADDRESS', 'PASSWORD') #It's better to save the credentials as env variables
    smtp.send_message(email)
