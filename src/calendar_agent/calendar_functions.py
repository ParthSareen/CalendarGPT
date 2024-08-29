from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import datetime
import pickle
import os.path
from typing import Optional, List, Dict, Any



# If modifying these scopes, delete the file token.pickle.
SCOPES: List[str] = ['https://www.googleapis.com/auth/calendar']
def authorize() -> Optional[Credentials]:
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds: Optional[Credentials] = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    try:
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
    except Exception:
        pass
        

    return creds

def get_calendar_events(start_time: str, end_time: str) -> List[Dict[str, Any]]:
    creds = authorize()
    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    events_result = service.events().list(calendarId='primary', timeMin=start_time,
                                        timeMax=end_time, singleEvents=True,
                                        orderBy='startTime').execute()
    events: List[Dict[str, Any]] = events_result.get('items', [])


    if not events:
        return {'message': 'No upcoming events found.', 'events': []}

    events_output = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        events_output.append({'start': start, 'summary': event['summary']})

    return str({'message': 'Events found.', 'events': events_output})


def create_calendar_event(summary: str, start_time: str, end_time: str, description: str = '', location: str = '', attendees: List[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    Create a calendar event.

    :param summary: The summary or title of the event.
    :param start_time: The start time of the event in RFC3339 format.
    :param end_time: The end time of the event in RFC3339 format.
    :param description: (Optional) The description of the event.
    :param location: (Optional) The location of the event.
    :param attendees: (Optional) A list of attendees' email addresses.
    :return: The created event.
    """
    creds = authorize()
    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'UTC',
        },
        'attendees': attendees or [],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (created_event.get('htmlLink')))
    return created_event
