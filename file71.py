import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('from@gmail.com',"Testing")
message = "Hello, how are you?"
s.sendmail("from@gmail.com","to@gmail.com",message)
s.quit()