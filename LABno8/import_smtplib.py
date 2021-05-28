import smtplib
import datetime
import smtpd

content = 'Vjezba 8 test' 

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()
mail.starttls()
mail.login('email', 'password')

mail.sendmail('veddob1@gmail.com', 'anteprojic@gmail.com', content)

mail.close()