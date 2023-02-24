import smtplib

sender_email = str(input("Enter Your Gmail : "))
password = str(input(" Enter Your Password : "))
receiver_email = str(input(" Enter Your Target E-Mail : "))
message = str(input(" Enter Your Massage : "))
amount = int(input(" Enter Your Amount : "))

IMTIAZ = smtplib.SMTP("smtp.gmail.com','578")
IMTIAZ = smtplib.SMTP('smtp.mail.yahoo.com', 465)
IMTIAZ = smtplib.SMTP('smtp.live.com', 587)

IMTIAZ.starttls()
IMTIAZ.login(sender_email, password)
print("Login successful")

for i in range(amount):
    IMTIAZ.sendmail(sender_email, receiver_email, message)
    print("Email sent to", receiver_email)

IMTIAZ.quit()

