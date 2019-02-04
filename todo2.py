import logging
import os

from flask import (
    Flask,
    render_template,
    request,
)
from twilio.rest import Client
from twilio.twiml.messaging_response import (
    # Do we need to import this?
    Message,
    MessagingResponse,
)

logging.basicConfig(level=logging.INFO)
CLIENT = Client()
NGROK_URL = os.environ.get('NGROK_URL')
TODOS = []
app = Flask(__name__)

@app.route("/")
def get():
    return "To-do Bot with status reporting"

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    sms_records = CLIENT.usage.records.last_month.list(category='sms')[0]
    count = sms_records.count
    price = sms_records.price
    return render_template(
        'dashboard.html',
        count=count,
        price=price,
        start_date=sms_records.start_date,
        end_date=sms_records.end_date,
    )

@app.route("/status", methods=['GET', 'POST'])
def status_reply():
    twilio_signature = request.headers.get('X-Twilio-Signature')
    sid = request.values.get('MessageSid')
    status = request.values.get('MessageStatus')

    logging.info(f"\nSID: {sid}\nStatus: {status}\nSignature: {twilio_signature}")
    return ('', 204)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    reply = MessagingResponse()

    message = request.values.get('Body').split()
    to_number = request.values.get('From')
    first_word = message[0].strip().lower()
    if first_word == 'add':
        item = " ".join(message[1:])
        TODOS.append(item)
        reply.message(f'Great, added "{item}" to list')
    elif first_word == 'remove':
        idx = int(message[1]) - 1
        item = TODOS.pop(idx)
        reply.message(f'Great, removed "{item}" from list')
    elif first_word == 'list':
        if not TODOS:
            reply.message("There is nothing on your to-do list.")
        else:
            list_items = []
            for idx, item in enumerate(TODOS):
                list_items.append(f"{idx + 1}. {item}")
            list_message = "\n".join(list_items)
            reply.message(list_message, action="/status", method="POST")
    else:
        reply.message("Sorry, I don't understand what you want me to do.")
    return str(reply)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
