# Ticket Booking System (Python)

A simple command-line program to manage events and book or cancel tickets.
All data is saved in JSON files, so no database or extra packages are needed.

## Requirements
- Python 3.8 or newer
- No external libraries

## How to Run
1. Unzip the project folder.
2. Open a terminal inside the `ticket_system` folder.
3. Run:

       python main.py

   (On some systems use `python3 main.py`.)

## Menu Options
| Option | What it does |
|---|---|
| 1. View events | Lists all events with date, price, and seats left |
| 2. Book tickets | Asks for event ID, your name, and quantity, then books |
| 3. Cancel a booking | Cancels a booking by ID and returns the seats |
| 4. My bookings | Shows all bookings for the name you enter |
| 5. Add event (admin) | Creates a new event |
| 0. Exit | Closes the program |

## Project Structure
    ticket_system/
    ├── main.py              Menu and user input/output
    ├── booking_service.py   Booking rules (book, cancel, add event, search)
    ├── storage.py           Reads and writes the JSON files
    ├── models.py            Event and Booking classes
    ├── data/
    │   ├── events.json      List of events (can be edited by hand)
    │   └── bookings.json    Saved bookings
    └── README.md            This file

## How the Files Work Together
    main.py  ->  booking_service.py  ->  storage.py  ->  data/*.json
                        |
                    models.py (data shapes used by all files)

- `main.py` only talks to the user. It never touches the JSON files directly.
- `booking_service.py` contains the rules (for example: not enough seats = booking refused).
- `storage.py` is the only file that reads and writes data.

## Editing Events Manually
Open `data/events.json` and add an entry in this format:

    {"event_id": 4, "name": "Theatre Show", "date": "2026-12-25 19:00",
     "price": 25.0, "total_seats": 80, "booked_seats": 0}

Each `event_id` must be unique. Keep `booked_seats` at 0 for a new event.

## Resetting the Data
- To clear all bookings, set `data/bookings.json` to `[]`.
- Then set `booked_seats` back to `0` for each event in `data/events.json`.

## Adding Your Own Comments
Every function has a comment on the line after its `def`. Add your own notes
with `#` above or beside any line.

## Possible Improvements
- Admin login
- Seat numbers instead of quantity only
- SQLite database instead of JSON
- Input validation for date format
