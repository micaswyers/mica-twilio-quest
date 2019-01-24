from flask import Flask, request
from twilio.twiml.messaging_response import (
    Message,
    MessagingResponse,
)

TODOS = []
app = Flask(__name__)

@app.route("/")
def get():
    return "To-do Bot"

@app.route("/sms")
def sms_reply():
    message = request.args.get('Body').split()
    first_word = message[0].strip().lower()
    if first_word == 'add':
        item = " ".join(message[1:])
        TODOS.append(item)
        response_message = 'Great, added "%s" to list' % (item,)
    elif first_word == 'remove':
        idx = int(message[1]) - 1
        item = TODOS.pop(idx)
        response_message = 'Great, removed "%s" from list' % (item,)
    elif first_word == 'list':
        if not TODOS:
            response_message = "There is nothing on your to-do list."
        else:
            list_items = []
            for idx, item in enumerate(TODOS):
                list_items.append(f"{idx + 1}. {item}")
            response_message = "\n".join(list_items)
    else:
        response_message = "Sorry, I don't understand what you want me to do."
    response = MessagingResponse()
    response.message(response_message)
    return str(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
