import os
from twilio.rest import Client

from flask import Flask, request
from twilio.twiml.messaging_response import (
    MessagingResponse,
)


account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
svc_sid = os.environ.get('SVC_SID')

service = client.messaging.services(svc_sid).fetch()
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    response = MessagingResponse()
    response.message("Hello World, this SMS was sent using a service")
    return str(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
