import os

from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

to_number = os.environ['MICA_CELL']
app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    resp = VoiceResponse()

    resp.dial(to_number)
    resp.say('Bye-bye')
    print(resp)
    return ('', 204)

if __name__ == "__main__":
    app.run(debug=True)



