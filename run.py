import requests
import pprint
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC4cebdb3f91c465dd8de9ebebe399148c'
auth_token = '6a42c296e68579a60d925ac8c39e61d3'
client = Client(account_sid, auth_token)

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    payload = {'api_key': 'seXC2fGDNpVjAnTtg4qLhZiBvKqLTLzp', 'q': message_body, 'limit': 1, 'lang': 'en'}
    r = requests.get('http://api.giphy.com/v1/gifs/search', params=payload)
    print(r.url)

    def gotData(stuff):
        print(stuff.json())

    resp = MessagingResponse()
    resp.message = (client.messages.create(
        body="Here you go!",
        from_='+14243214684',
        media_url=(r.json()['data'][0]['images']['original']['url']),
        to='+14848853093'))
    return str(resp)


if __name__ == "__main__":
    app.run()
