import smtplib
import ssl
from email.message import EmailMessage
from weather import Weather

# from: http://api.openweathermap.org
weather = Weather(API_KEY="YOUR_API_KEY")

subject = "Weather Infor By Email (WIBE)"
sender_email = input("Enter a sender email address: ")
receiver_email = input("Enter a receiver email address: ")
sender_password = input("Enter a sender email password: ")

city_target = input("What is the city ? ");
weather_data = weather.request_infors(city_target)

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
  <body>
    <h1>{subject}</h1>
    <p>Weather: {weather_data.weather}</p>
    <p>Temperature: {weather_data.temperature} celsius</p>
  </body>
</html>
"""

message.add_alternative(html, subtype="html")
context = ssl.create_default_context()

print("I'm Sending the Email!, wait a seconds")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
  server.login(sender_email, sender_password)
  server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")
