# models.py
# Defines the data objects (Event and Booking) used across the program.

from dataclasses import dataclass, asdict


@dataclass
class Event:
    """An event people can book tickets for (movie, concert, match...)."""
    event_id: int
    name: str
    date: str          # format: YYYY-MM-DD HH:MM
    price: float       # price per ticket
    total_seats: int   # total capacity
    booked_seats: int = 0

    def seats_left(self):
        # Returns how many seats are still available.
        return self.total_seats - self.booked_seats

    def to_dict(self):
        # Converts the Event to a dictionary so it can be saved as JSON.
        return asdict(self)


@dataclass
class Booking:
    """A booking made by a customer for one event."""
    booking_id: int
    event_id: int
    customer_name: str
    quantity: int
    total_price: float
    status: str = "CONFIRMED"   # CONFIRMED or CANCELLED

    def to_dict(self):
        # Converts the Booking to a dictionary so it can be saved as JSON.
        return asdict(self)
