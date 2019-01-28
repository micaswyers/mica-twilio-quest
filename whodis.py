from flask import Flask, request
from twilio.twiml.messaging_response import (
    Message,
    MessagingResponse,
)

app = Flask(__name__)

@app.route("/")
def get():
    return "New App, who dis?"

@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    fromCountry = request.args.get('FromCountry')
    response = MessagingResponse()
    response.message("Hi! It looks like your phone number was born in %s" % (fromCountry,))
    return str(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
