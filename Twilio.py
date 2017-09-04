# Twilio
from twilio.rest import Client
account_sid = "##############################"
auth_token = "##############################"
client = Client(account_sid, auth_token)
client.messages.create(
    to="+12345678901",
    from_="+819012345678",
    body="退屈な作業が終わったよ")
