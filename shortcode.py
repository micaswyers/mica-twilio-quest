import os

from twilio.rest import Client


from_number = os.environ['TOLLFREE_NUMBER']
to_number = os.environ['MICA_CELL']
client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])

for i in range(1,11):
    message = client.messages.create(
        from_=from_number,
        body=f"This is message {i}.",
        to=to_number,
    )
    print(message.sid)
