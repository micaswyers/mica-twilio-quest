import json
import requests
from flask import Flask, request

from twilio.twiml.messaging_response import MessagingResponse


API_LINK = "https://en.wikipedia.org/api/rest_v1/page/"
app = Flask(__name__)

LAST_TITLE = None


@app.route("/incoming", methods=["GET", "POST"])
def play():
    global LAST_TITLE
    response = MessagingResponse()

    body = request.values.get("Body")
    print(f"Body: {body}")

    if body.lower() == "play":
        # Call Wikipedia API to get a page, store in variable
        page = _get_wiki_page()
        # Call Wikipedia API to get first image on that page.
        img_link = _get_media_link(page['title'])
        # Return image to user
        msg = response.message("What page is this?")
        msg.media(img_link)
        LAST_TITLE = page['title'].lower()
        print(f"Current title: {LAST_TITLE}")
    else:
        if not LAST_TITLE:
            response.message("Say PLAY to start a Wikipedia guessing game!")
        else:
            # Check input against page_title
            if body.lower() == "stop":
                response.message("Oh well, you tried.")
                LAST_TITLE = None
            elif body in LAST_TITLE:
                response.message(f"Amazing, you did it! The title was: '{LAST_TITLE}'.")
                LAST_TITLE = None
            else:
                response.message("Not quite, try again! Or say STOP to quit.")
    return str(response)


def _get_wiki_page():
    wiki_request = json.loads(requests.get(API_LINK + "random/title").text)
    page = wiki_request['items'][0]
    return page


def _get_media_link(page_title):
    wiki_request = json.loads(requests.get(f"{API_LINK}media/{page_title}").text)

    media = wiki_request['items'][0]
    thumbnail = media['thumbnail']['source']
    return thumbnail


if __name__ == "__main__":
    app.run(debug=True)
