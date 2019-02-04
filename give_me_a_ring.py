import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_number = os.environ['MICA_CELL']
from_number = os.environ['TQ_NUMBER']

client = Client(account_sid, auth_token)

call = client.calls.create(
    url='{{URL_HERE}}',
    to=my_number,
    from_=from_number,
)

print(call.sid)
