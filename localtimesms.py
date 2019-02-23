import os
from datetime import datetime
from twilio.rest import Client

CLIENT = Client()
TQ_NUMBER = os.environ['TQ_NUMBER']
NUMBER = "+12092104311"

current_time = datetime.now().time()

body = f"Greetings! The current time is: {current_time} 46L7CZH6XDXGQIB"

message = CLIENT.messages.create(
    body=body,
    from_=TQ_NUMBER,
    to=NUMBER,
)

print(message.sid)
