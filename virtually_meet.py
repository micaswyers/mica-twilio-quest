import os

from flask import Flask, request
from twilio.twiml.voice_response import Conference, Dial, VoiceResponse

app = Flask(__name__)

MODERATOR = os.environ['MICA_CELL']

@app.route('/voice', methods=['GET', 'POST'])
def conf_call():
    response = VoiceResponse()
    with Dial() as dial:
        if request.values.get('From') == MODERATOR:
            dial.conference(
                "My Conference Room",
                start_conference_on_enter=True,
                end_conference_on_exit=True,
                waitUrl="http://twimlets.com/holdmusic?Bucket=com.twilio.music.electronica&amp;Message=please%20wait",
            )
        else:
            dial.conference('My Conference Room', start_conference_on_enter=False)
    response.append(dial)
    return str(response)


if __name__ == '__main__':
    app.run(debug=True)
