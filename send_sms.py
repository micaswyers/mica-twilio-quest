# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import creds


# Your Account Sid and Auth Token from twilio.com/console
account_sid = creds.ACCOUNT_SID
auth_token = creds.AUTH_TOKEN
client = Client(account_sid, auth_token)
to_number = creds.TO_NUMBER

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=creds.TWILIO_NUMBER,
                     to='%s' % (to_number,),
                 )

print(message.sid)

