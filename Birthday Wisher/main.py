from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"
TO_ADDRESS = "DESTINATION"

numer = random.randint(1, 3)
with open(f"letter_templates/letter_{numer}.txt") as f:
    listish = f.read()

today = datetime.now()
today_tuple = (today.day, today.month)

dane = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in dane.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    content = listish.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_ADDRESS,
                            msg=f"Subject:Happy Birthday! \n\n {content}")
