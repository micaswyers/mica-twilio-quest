import os

from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_number = os.environ['MICA_CELL']
svc_sid = os.environ['SVC_SID']
other_number = os.environ['KPOP_NUMBER']


client = Client(account_sid, auth_token)

for i in range(1,11):
    message = client.messages.create(
            body=f'I ate {i} cake(s)!',
            messaging_service_sid=svc_sid,
            to=my_number,
    )
    print(f'Message SID {message.sid} sent to {message.to}')

    message2 = client.messages.create(
            body=f'I ate {i} cake(s)!',
            messaging_service_sid=svc_sid,
            to=other_number,
    )
    print(f'Message SID {message2.sid} sent to {message2.to}')
