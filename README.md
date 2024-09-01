# CalendarGPT

CalendarGPT is a Python-based application that allows users to interact with their Google Calendar using natural language commands over text messaging. It leverages the Google Calendar API, Twilio API, and [DAGent](https://github.com/ParthSareen/DAGent) for managing calendar events. 

## Features

- View upcoming calendar events
- Create new calendar events with customizable details (summary, start/end time, description, location, attendees)
- Interface with CalendarGPT through phone messaging 

## Getting Started

To get started with CalendarGPT, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/CalendarGPT.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the Google Calendar API credentials:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Google Calendar API for your project
   - Create credentials (OAuth client ID) for a desktop application
   - Download the `credentials.json` file and place it in the project directory
4. Set up the Twilio API credentials:
   - Sign up for a [Twilio account](https://www.twilio.com/try-twilio)
   - Get your Account SID and Auth Token from the Twilio console
   - Set the following environment variables:
     - `TWILIO_ACCOUNT_SID`: Your Twilio Account SID
     - `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token
     - `TWILIO_NUMBER`: Your Twilio phone number
     - `MY_PHONE_NUMBER`: The phone number you want to receive SMS reminders on
5. Run the application: `python src/calendar_agent/server.py`

## Key Files

### `cli.py`

CLI version of the application. You can try things out here before using the server. It sets up the decision nodes and function nodes for the agent, handles user input, and manages the interaction flow.

### `calendar_functions.py`

This file contains the core functions for interacting with the Google Calendar API, including:

- `authorize()`: Handles the OAuth2 authentication flow with Google Calendar
- `get_calendar_events(start_time, end_time)`: Retrieves a list of upcoming events within the specified time range
- `create_calendar_event(summary, start_time, end_time, description, location, attendees)`: Creates a new calendar event with the provided details

### `twilio_functions.py`

This file contains the function for sending SMS reminders using the Twilio API:

- `send_message(prev_output, *args, **kwargs)`: Sends an SMS message to the configured phone number using the Twilio API

### `server.py`

This file sets up a Flask server to handle incoming SMS messages and respond with calendar information. It exposes an endpoint `/sms/` that accepts incoming SMS messages and sends a response back with the relevant calendar information.

## Contributing

Contributions to CalendarGPT are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request.

When contributing, please follow the existing code style and conventions. Additionally, make sure to update the documentation accordingly.

## License

CalendarGPT is released under the [MIT License](LICENSE).