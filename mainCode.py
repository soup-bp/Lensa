from twilio.rest import Client

account_sid = "sid"
auth_token  = "token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14258372423", 
    from_="+16692366969",
    body="Hello from Python!")

print(message.sid)
