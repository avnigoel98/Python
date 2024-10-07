# sending mail to 100 people at a time
import smtplib as s

server = s.SMTP( 'smtp.gmail.com',  587)
server.ehlo()
server.starttls() 
server.login("avnigoel98@gmail.com", "qyss xock eeza mcst")

subject = "Testing Email Sender"
body = "testing python email sender"

msg = "subject: {}\n\n{}".format(subject, body)

sender = "avnigoel98@gmail.com"
listAddress= ['avnigoel98@gmail.com', "memito214.gg@gmail.com"]

server.sendmail(sender, listAddress, msg)

print("Sent Mail Successfully")

server.quit()