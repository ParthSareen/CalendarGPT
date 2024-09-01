from flask import Flask, request, jsonify
from dagent import *
from calendar_functions import get_calendar_events, create_calendar_event
from twilio_functions import send_message
from twilio.twiml.messaging_response import MessagingResponse

import datetime
from pytz import timezone

app = Flask(__name__)

def clean_output(prev_output: str) -> str:
    messages = [{'role': 'user', 'content': f"You are a cheerful and helpful AI assistant called CalenderGPT helping the user manage their calendar. Use the following information to tell them about the: {prev_output}"}]
    cleaned_output = call_llm('gpt-3.5-turbo-0125', messages)
    print(cleaned_output)
    return cleaned_output


# Define the nodes
entry_decision = DecisionNode()

get_calendar_events_node = FunctionNode(func=get_calendar_events)
create_calendar_event_node = FunctionNode(func=create_calendar_event)
clean_output_node = FunctionNode(func=clean_output)
send_message_node = FunctionNode(func=send_message)


# Connect the nodes
entry_decision.next_nodes = [get_calendar_events_node, create_calendar_event_node]

get_calendar_events_node.next_nodes = [clean_output_node]
create_calendar_event_node.next_nodes = [clean_output_node]

clean_output_node.next_nodes = [send_message_node]

entry_decision.compile()


# Webhook for Twilio
@app.route("/sms/", methods=['GET', 'POST'])
def sms_reply():
    user_input = request.values.get('Body', None)
            
    resp = MessagingResponse()
    if not user_input:
        resp.message("Sorry, I didn't receive a message from you. Please try sending your request again.")
        return str(resp)
    
    utc_now = datetime.datetime.now(timezone('UTC'))
    est_now = utc_now.astimezone(timezone('US/Eastern'))
    today_utc = utc_now.isoformat() + 'Z'
    today_est = est_now.isoformat() + 'Z'

    messages = [{"role": "user", "content": f"{user_input}. Given that today is {today_utc} in UTC, which is {today_est} EST, and it's {datetime.datetime.now().strftime('%A')}."}]
    entry_decision.run(messages=messages)
    calendar_data = clean_output_node.node_result
    
    resp.message(str(calendar_data))
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)

