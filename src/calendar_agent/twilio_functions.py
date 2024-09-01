import os
from twilio.rest import Client


my_twilio_number = os.environ['TWILIO_NUMBER'] 
number_to_text = os.environ['MY_PHONE_NUMBER']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def send_message(prev_output, *args, **kwargs):
    try:
        message = client.messages \
            .create(
                body=prev_output,
                from_=my_twilio_number,
                to=number_to_text
            )

        print('message sent', message.sid)
    except Exception as e:
        print(f'Error sending message: {e}')
