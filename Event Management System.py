class Attendee():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
class Ticket():
    def __init__(self, event, attendee, price):
        self.event = event
        self.attendee = attendee
        self.price = price
        self.is_valid = True
        
    def validate(self):
        if self.event.is_started() and self.is_valid:
            print(f"Your ticket is VALID :-) for the event {self.event.name}.")
        else:
            print(f"Your ticket is NOT VALID! for the event {self.event.name}.")

class Event():
    def __init__(self, name, date, seats):
        self.name = name
        self.date = date
        self.seats = seats
        self.tickets_sold = 0
        self.attendees = []
    
    def is_started(self):
        return True
        
    def tkt_selling(self, attendee):
        if self.tickets_sold < self.seats:
            tkt = Ticket(self, attendee, 120.0)
            self.attendees.append(attendee)
            self.tickets_sold += 1
            return tkt
        else:
            print(f"SORRY :-( , We ran out of tickets! We miss you!")
            return None
    
    def check_in(self, ticket):
        if ticket.is_valid:
            print(f"{ticket.attendee.name} has been checked in for {self.name}!")
        else:
            print(f"{ticket.attendee.name}'s ticket is NOT VALID!!")

event_name = input('Enter the event name: ')
event_date = input('Enter the event date (DD-MM-YYYY): ')
event_seats = int(input("Enter number of seats: "))

event = Event(event_name, event_date, event_seats)
n_attendees = int(input('Enter the number of attendees: '))

print("~ Enter Attendee's credentials ~")
for i in range(n_attendees):
    print(f"Attendee {i + 1}: ")
    a_name = input("   Enter Attendee name: ")
    a_email = input("   Enter Attendee email: ")
    attendee = Attendee(a_name, a_email)
    
    ticket = event.tkt_selling(attendee)
    if ticket:
        ticket.validate()
        event.check_in(ticket)

