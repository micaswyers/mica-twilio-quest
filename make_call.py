from twilio.rest import Client

import creds

account_sid = creds.ACCOUNT_SID
auth_token = creds.AUTH_TOKEN
to_number = creds.TO_NUMBER
client = Client(account_sid, auth_token)

call = client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',
    to='%s' % (to_number),
    from_=creds.TWILIO_NUMBER
)

print(call.sid)
