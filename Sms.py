from twilio.rest import Client


account_sid = 'Account ID'
auth_token = 'Account Token'            #save them as Env Variables

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="the number you want to send the SMS",
    from_="YOUR TWILIO PHONE NUMBER",
    body="MESSAGE")