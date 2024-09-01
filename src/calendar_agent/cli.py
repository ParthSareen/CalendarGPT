from dagent import *
from calendar_functions import get_calendar_events, create_calendar_event
import datetime
from pytz import timezone


def clean_output(prev_output: str) -> str:
    messages = [{'role': 'user', 'content': f"You are a cheerful and helpful AI assistant helping the user manage their calendar. Use the following information to tell them about the: {prev_output}"}]
    cleaned_output = call_llm('gpt-3.5-turbo-0125', messages)
    print(cleaned_output)
    return cleaned_output

entry_decision = DecisionNode()

get_calendar_events_node = FunctionNode(func=get_calendar_events)
create_calendar_event_node = FunctionNode(func=create_calendar_event)
clean_output_node = FunctionNode(func=clean_output)

entry_decision.next_nodes = [get_calendar_events_node, create_calendar_event_node]

get_calendar_events_node.next_nodes = [clean_output_node]
create_calendar_event_node.next_nodes = [clean_output_node]

entry_decision.compile()

while True:
    user_input = input("Enter a command: ")
    utc_now = datetime.datetime.now(timezone('UTC'))
    est_now = utc_now.astimezone(timezone('US/Eastern'))
    today_utc = utc_now.isoformat() + 'Z'
    today_est = est_now.isoformat() + 'Z'

    messages = [{"role": "user", "content": "{}. Given that today is {} in UTC, which is {} EST, and it's {}.".format(user_input, today_utc, today_est, datetime.datetime.now().strftime("%A"))}]
    # entry_decision.run(prev_output=user_input)
    entry_decision.run(messages=messages)
