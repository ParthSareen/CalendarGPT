# CalendarGPT 

CalendarGPT is a Python-based application that allows users to interact with their Google Calendar using natural language commands. It leverages the Google Calendar API and [DAGent](https://github.com/ParthSareen/DAGent) for managing calendar events. CalendarGPT can also use local models through DAGent.

## Features

- View upcoming calendar events
- Create new calendar events with customizable details (summary, start/end time, description, location, attendees)

## Getting Started

To get started with CalendarGPT, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/CalendarGPT.git`
2. Install the required dependencies: `pip install -r requirements.lock`
3. Set up the Google Calendar API credentials:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Google Calendar API for your project
   - Create credentials (OAuth client ID) for a desktop application
   - Download the `credentials.json` file and place it in the project directory

4. Run the application: `python src/calendar_agent/main.py`

## Key Files

### `main.py`

This file contains the main entry point for the application. It sets up the decision nodes and function nodes for the agent, handles user input, and manages the interaction flow.

### `calendar_functions.py`

This file contains the core functions for interacting with the Google Calendar API, including:

- `authorize()`: Handles the OAuth2 authentication flow with Google Calendar
- `get_calendar_events(start_time, end_time)`: Retrieves a list of upcoming events within the specified time range
- `create_calendar_event(summary, start_time, end_time, description, location, attendees)`: Creates a new calendar event with the provided details

## Contributing

Contributions to CalendarGPT are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request.

When contributing, please follow the existing code style and conventions. Additionally, make sure to update the documentation accordingly.

## License

CalendarGPT is released under the [MIT License](LICENSE).