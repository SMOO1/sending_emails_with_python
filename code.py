from email.message import EmailMessage
import ssl
import smtplib
from time import sleep

#email sender and recipient
sender_email = "insertemail@gmail.com"
sender_pas = "insert google authentication code"
reciever_email = "insertemail@gmail.com"

#email message
subject = "Goo Ga"
body = "."
em = EmailMessage()
em["from"] = sender_email
em["To"] = reciever_email
em["Subject"] = subject
em.set_content(body)

# Attach the image
with open("D:\\image_directory.jpg", "rb") as f:
    image_data = f.read()
em.add_attachment(image_data, maintype="image", subtype="jpg", filename="image.jpg")

context = ssl.create_default_context()

# number of emails sent
emails = integer value

for i in range(emails):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as joe:
        joe.login(sender_email, sender_pas)
        joe.send_message(em)
        print(i)
        sleep(1)
