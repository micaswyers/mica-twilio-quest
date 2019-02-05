import os

from flask import (
    Flask,
    request,
)
from twilio.rest import Client
from twilio.twiml.messaging_response import (
    Message,
    MessagingResponse,
)
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)
CLIENT = Client()
NUM_CALLS = 0
TQ_NUMBER = os.environ.get('TQ_NUMBER')
USER_NUMBER = os.environ.get('MICA_CELL')



@app.route("/voice", methods=["GET", "POST"])
def answer_call():
    # Hang up after giving a message to the caller
    global NUM_CALLS
    response = VoiceResponse()
    response.say("Hello! I'm very busy and important!")
    response.hangup()
    NUM_CALLS += 1
    caller=request.values.get("Caller")
    _text_caller(caller=caller)
    _text_user(from_number=caller)
    # Why can't I return "('', 204)" here?
    return str(response)

def _text_caller(caller=None):
    # Text caller with other methods to contact the user

    body = f"Hi, Mica is deliberately avoiding your phonecall.\
            Try messaging her at {os.environ['MICA_CELL']} or tweeting at her."
    message = CLIENT.messages.create(
        body=body,
        from_=TQ_NUMBER,
        to=caller,
    )

def _text_user(from_number=None):
    body = f"Hi, Mica, you just received a call from {from_number or None}.\
            I've saved you from having to answer {NUM_CALLS} calls! 🥐"
    message = CLIENT.messages.create(
        body=body,
        from_=TQ_NUMBER,
        to=USER_NUMBER,
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')
