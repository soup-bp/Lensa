from twilio.rest import Client

account_sid = "AC08d84c84a3fe547c8c61b534e65d622e"
auth_token  = "f12d4fadb37eb23cf377215e34bf14dd"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14258372423", 
    from_="+16692366969",
    body="Hello from Python!")

print(message.sid)
