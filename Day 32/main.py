import smtplib

my_email = "123@gmail.com"
password = "12345"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addr="test@gmail.com", msg="Hello")
connection.close()

#___________________________________
import smtplib

my_email = "123@gmail.com"
password = "12345"

with smtplib.SMTP("smtp.gmail.com") as connection:
  connection.starttls()
  connection.login(user=my_email, password=password)
  connection.sendmail(from_addr=my_email, to_addr="test@gmail.com", msg="Hello")


#___________________________________
import datetime as dt

now = dt.datetime.now()
year = now.year()
month = now.month()
day_of_week = now.weekday()
day_of_birth = dt.datetime(year=1995, month=12, day=15)


#___________________________________
import smtplib
import datetime as dt
import random

MY_EMAIL = "123@gmail.com"
MY_PASSWORD = "12345"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
  with open("quotes.txt") as quote_file:
    all_quotes = quote_files.readlines()
    quote = random.choice(all_quotes)

  print(quote)
  connection = smtplib.SMTP("smtp.gmail.com")
  connection.starttls()
  connection.login(MY_EMAIL, MY_PASSWORD)
  connection.sendmail(from_addr=MY_EMAIL, to_addr=MY_EMAIL, msg=f"Subject: Monday\n\n{quote}")
