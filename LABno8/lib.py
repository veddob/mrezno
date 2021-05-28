import smtplib
import datetime
import smtpd

SERVER = 'localhost'
PORT = 25

FROM = "veddob1@gmail.com"
TO = ["asdf@asdf.com"]

SUBJECT = "test"
TEXT = "Vjezba8test"

message = """\
Sends: %s
Rec.: %s
Subj.: %s
%s
""" % (FROM, ",".join(TO), SUBJECT, TEXT)
server = smtplib.SMTP(SERVER, PORT)
server.sendmail(FROM,TO,message)
server.quit()