 import smtplib
 import IMTIAZ-X

IMTIAZ=smtplib.SMTP("smtp.gmail.com','578")

IMTIAZ.ehlo
IMTIAZ.starttls()

email=str(input("Enter Your Gmail : "))
pwd=str(input(" Enter Your Password : "))
tamil=str(input(" Enter Your Target E-Mail : "))
msg=str(input(" Enter Your Massage : "))
amount=str(input(" Enter Your Amount"))

IMTIAZ.login(email,pwd)

for i in range(amount):
    IMTIAZ.sendmail(email,tmail,msg)
    
