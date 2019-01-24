import os
from datetime import datetime
from twilio.rest import Client

CLIENT = Client(os.environ['ACCOUNT_SID'], os.environ['AUTH_TOKEN'])
NUMBER = os.environ['LOCAL_TIME_NUMBER']

body = "Greetings! The current time is: 5:04 pm"

CLIENT.messages.create(
    body=body,
    from_=creds.TWILIO_NUMBER,
    to=NUMBER,
)

