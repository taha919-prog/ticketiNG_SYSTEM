# main.py
# Entry point. Shows the menu and talks to the user. Run with:  python main.py

import booking_service as service


def show_events():
    # Prints every event with its price and remaining seats.
    events = service.get_events()
    if not events:
        print("No events yet.")
        return
    print(f"\n{'ID':<4}{'Name':<28}{'Date':<18}{'Price':>8}{'Seats left':>12}")
    print("-" * 70)
    for e in events:
        print(f"{e.event_id:<4}{e.name:<28}{e.date:<18}{e.price:>8.2f}{e.seats_left():>12}")


def ask_int(prompt):
    # Asks for a whole number and repeats until the user enters a valid one.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")


def ask_float(prompt):
    # Asks for a decimal number (e.g. a price) and repeats until valid.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def book_menu():
    # Asks the user which event, name, and quantity, then books it.
    show_events()
    event_id = ask_int("\nEvent ID to book: ")
    name = input("Your name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    quantity = ask_int("Number of tickets: ")
    ok, result = service.book_ticket(event_id, name, quantity)
    if ok:
        print(f"\nBooked! Booking ID: {result.booking_id} | Total: {result.total_price:.2f}")
    else:
        print(f"\nCould not book: {result}")


def cancel_menu():
    # Asks for a booking ID and cancels it.
    booking_id = ask_int("Booking ID to cancel: ")
    ok, message = service.cancel_booking(booking_id)
    print(message)


def my_bookings_menu():
    # Shows all bookings for the name entered.
    name = input("Your name: ").strip()
    bookings = service.get_bookings_by_customer(name)
    if not bookings:
        print("No bookings found.")
        return
    for b in bookings:
        event = service.find_event(b.event_id)
        event_name = event.name if event else "Unknown event"
        print(f"#{b.booking_id} | {event_name} | {b.quantity} ticket(s) | "
              f"{b.total_price:.2f} | {b.status}")


def add_event_menu():
    # Admin option: creates a new event.
    name = input("Event name: ").strip()
    date = input("Date (YYYY-MM-DD HH:MM): ").strip()
    price = ask_float("Ticket price: ")
    seats = ask_int("Total seats: ")
    event = service.add_event(name, date, price, seats)
    print(f"Event added with ID {event.event_id}.")


def main():
    # Main loop: shows the menu until the user chooses Exit.
    actions = {
        "1": show_events,
        "2": book_menu,
        "3": cancel_menu,
        "4": my_bookings_menu,
        "5": add_event_menu,
    }
    while True:
        print("\n=== TICKET BOOKING SYSTEM ===")
        print("1. View events")
        print("2. Book tickets")
        print("3. Cancel a booking")
        print("4. My bookings")
        print("5. Add event (admin)")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
