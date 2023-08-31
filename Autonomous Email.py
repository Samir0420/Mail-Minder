import smtplib # Used to send an email 
from email.message import EmailMessage # Allows me to include a subject, to, from for my emails

# These imports will be used to schedule my emails
import schedule
import time

# This import will be used to get current date for emails
from datetime import date

# Get the current year
def getYear():
   today = date.today()

   return(today.year)

#Get the current month
def getMonth():
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    
    today = date.today()
    return months[today.month]

# Get the current day
def getDay():
   today = date.today()

   return(today.day)

def sendEmail():
   try:
      # creates SMTP session
      s = smtplib.SMTP('smtp.gmail.com', 587) #For gmail, the port is 587
       
      # Start TLS for security
      # All SMTP files that follow will be encrypted
      s.starttls()
       
      # Authentication (Sender Email, Sender Password)
      # If using Gmail, get the password code through Google Account > Security > 2 Step verification > App Passwords
      s.login("myemail@example.com", "password_here")
       
      # Message that will be sent
      message = EmailMessage() # Create a new message

      message.set_content("This is an email telling you that you are awesome") # Contains the content of the email
      
      message['Subject'] = f"Meeting Reminder - {getMonth()} {getDay()}, {getYear()}"         # Add Subject
      message['From'] = "senderemail@example.com"                                             # Add Sender Email
      message['To'] = "recieveremail@example.com"                                             # Add Reciever Email
        
      # Send the mail with message
      s.send_message(message)

      print("Mail successfully sent!")
      
      # Terminate the session
      s.quit()
      
   except:
      print("Mail did not send :(")


# Schedule emails here
# Check the documentation of the schedule module to learn more
schedule.every().wednesday.at("12:00").do(sendEmail)
schedule.every().thursday.at("12:00").do(sendEmail)

while True:
   schedule.run_pending()
   time.sleep(1)
