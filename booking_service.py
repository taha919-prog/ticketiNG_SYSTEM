# booking_service.py
# The "brain" of the system: all booking rules live here (no print/input in this file).

from models import Booking
import storage


def get_events():
    # Returns the list of all events.
    return storage.load_events()


def find_event(event_id):
    # Looks up one event by its ID. Returns None if not found.
    for event in storage.load_events():
        if event.event_id == event_id:
            return event
    return None


def add_event(name, date, price, total_seats):
    # Creates a new event with the next free ID and saves it. Returns the new Event.
    from models import Event
    events = storage.load_events()
    new_id = max((e.event_id for e in events), default=0) + 1
    event = Event(new_id, name, date, price, total_seats)
    events.append(event)
    storage.save_events(events)
    return event


def book_ticket(event_id, customer_name, quantity):
    # Books tickets. Checks the event exists and enough seats are left.
    # Returns (True, Booking) on success or (False, error message) on failure.
    if quantity < 1:
        return False, "Quantity must be at least 1."

    events = storage.load_events()
    event = next((e for e in events if e.event_id == event_id), None)
    if event is None:
        return False, "Event not found."
    if quantity > event.seats_left():
        return False, f"Only {event.seats_left()} seat(s) left."

    bookings = storage.load_bookings()
    new_id = max((b.booking_id for b in bookings), default=0) + 1
    booking = Booking(new_id, event_id, customer_name, quantity, quantity * event.price)

    event.booked_seats += quantity          # reduce available seats
    bookings.append(booking)
    storage.save_events(events)
    storage.save_bookings(bookings)
    return True, booking


def cancel_booking(booking_id):
    # Cancels a booking and gives the seats back to the event.
    # Returns (True, message) or (False, error message).
    bookings = storage.load_bookings()
    booking = next((b for b in bookings if b.booking_id == booking_id), None)
    if booking is None:
        return False, "Booking not found."
    if booking.status == "CANCELLED":
        return False, "Booking is already cancelled."

    events = storage.load_events()
    for event in events:
        if event.event_id == booking.event_id:
            event.booked_seats -= booking.quantity   # free the seats
    booking.status = "CANCELLED"
    storage.save_events(events)
    storage.save_bookings(bookings)
    return True, f"Booking #{booking_id} cancelled."


def get_bookings_by_customer(customer_name):
    # Returns all bookings for a customer (case-insensitive name match).
    return [b for b in storage.load_bookings()
            if b.customer_name.lower() == customer_name.lower()]
