from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
to_number = os.environ['MICA_CELL']
from_number = os.environ['TQ_NUMBER']

client = Client(account_sid, auth_token)

call = client.calls.create(
    to=to_number,
    from_=from_number,
    url="http://demo.twilio.com/docs/voice.xml",
)

print(call.sid)
