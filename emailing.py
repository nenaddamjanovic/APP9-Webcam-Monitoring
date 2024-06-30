import smtplib
from email.message import EmailMessage
# import imghdr  # Ne koristi se u python 13, zamena je PIL
from PIL import Image

# Your app password for your device: lgcg ysie dygj owce
password = "lgcgysiedygjowce"
email_sender = "informaticarmreze@gmail.com"
email_receiver = "informaticarmreze@gmail.com"


def send_email(image_path):
    # Create an email message object
    print("send email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer entered in shop"
    email_message.set_content("Hey, we just seen a new customer!!")

    # Open the image file in binary mode and read its content
    with open(image_path, "rb") as file:
        content = file.read()

    # Use Pillow to open the image and get its format
    with Image.open(image_path) as img:
        image_format = img.format.lower()

    # Add the image as an attachment with the correct MIME type
    email_message.add_attachment(content, maintype="image",
                                 subtype=image_format)

    # Set up the SMTP connection
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()  # Identify ourselves to the server
    gmail.starttls()  # Secure the connection with TLS
    gmail.login(email_sender, password)  # Log in to the SMTP server
    gmail.sendmail(email_sender, email_receiver, email_message.as_string())  # Send the email
    gmail.quit()

    print("send email function ended")


if __name__ == "__main__":
    send_email(image_path="images/1.png")