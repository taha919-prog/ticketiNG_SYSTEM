# storage.py
# Handles reading and writing the JSON files in the data/ folder.

import json
import os

from models import Event, Booking

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
EVENTS_FILE = os.path.join(DATA_DIR, "events.json")
BOOKINGS_FILE = os.path.join(DATA_DIR, "bookings.json")


def _read_json(path):
    # Reads a JSON file and returns a list. Returns [] if the file is missing or empty.
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def _write_json(path, items):
    # Writes a list of dictionaries to a JSON file.
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)


def load_events():
    # Loads all events from events.json and returns them as Event objects.
    return [Event(**e) for e in _read_json(EVENTS_FILE)]


def save_events(events):
    # Saves a list of Event objects to events.json.
    _write_json(EVENTS_FILE, [e.to_dict() for e in events])


def load_bookings():
    # Loads all bookings from bookings.json and returns them as Booking objects.
    return [Booking(**b) for b in _read_json(BOOKINGS_FILE)]


def save_bookings(bookings):
    # Saves a list of Booking objects to bookings.json.
    _write_json(BOOKINGS_FILE, [b.to_dict() for b in bookings])
