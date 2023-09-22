#SoftwareDevelopmentPRoject
#Help Desk Software Project
#@ author: LorenceJuguilon
# Date 09/09/2023
#
class Ticket:
    ticket_counter = 2000

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_id = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.status = "Open"
        self.response = "Not Yet Provided"  # Default response

        if "Password Change" in description:
            self.generate_password()
            self.close_ticket()

    def generate_password(self):
        staff_id_prefix = self.staff_id[:2]
        creator_name_prefix = self.creator_name[:3]
        self.new_password = staff_id_prefix + creator_name_prefix

    def respond(self, response):
        self.response = response
        if self.status != "Closed":
            self.close_ticket()

    def close_ticket(self):
        self.status = "Closed"

    def reopen_ticket(self):
        self.status = "Reopened"

    def get_ticket_info(self):
        return f"Ticket Number: {self.ticket_id}\nName of Creator: {self.creator_name}\nStaffID: {self.staff_id}\nEmail Address: {self.contact_email}\nDescription: {self.description}\nResponse: {self.response}\nTicket Status: {self.status}"

    @staticmethod
    def TicketStats(tickets):
        total_tickets = len(tickets)
        resolved_tickets = sum(1 for ticket in tickets if ticket.status == "Closed")
        open_tickets = total_tickets - resolved_tickets
        return total_tickets, resolved_tickets, open_tickets


class TicketManager:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, staff_id, creator_name, contact_email, description):
        ticket = Ticket(staff_id, creator_name, contact_email, description)
        self.tickets.append(ticket)

    def respond_to_ticket(self, ticket_id, response):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.respond(response)
                print(f"Ticket ID {ticket_id} responded successfully.")
                break

    def close_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.close_ticket()
                print(f"Ticket ID {ticket_id} closed successfully.")
                break

    def reopen_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.reopen_ticket()
                print(f"Ticket ID {ticket_id} reopened successfully.")
                break


def main():
    ticket_manager = TicketManager()

    # Create some sample tickets
    ticket_manager.create_ticket("STF123", "John Doe", "john@example.com", "Password Change Request")
    ticket_manager.create_ticket("STF456", "Jane Smith", "jane@example.com", "Network Issue")
    ticket_manager.create_ticket("STF789", "Alice Johnson", "alice@example.com", "Software Installation")

    while True:
        print("\nHelp Desk Ticketing System")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Update Ticket Status")
        print("4. Respond to Ticket")
        print("5. Close Ticket")
        print("6. Reopen Ticket")
        print("7. Display Ticket Statistics")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            staff_id = input("Enter Staff ID: ")
            creator_name = input("Enter Creator Name: ")
            contact_email = input("Enter Contact Email: ")
            description = input("Enter Description: ")
            ticket_manager.create_ticket(staff_id, creator_name, contact_email, description)
            print("Ticket created successfully.")

        elif choice == "2":
            print("\nAll Tickets:")
            for ticket in ticket_manager.tickets:
                print(ticket.get_ticket_info())

        elif choice == "3":
            ticket_id = int(input("Enter Ticket ID to respond: "))
            response = input("Enter response: ")
            ticket_manager.respond_to_ticket(ticket_id, response)

        elif choice == "4":
            ticket_id = int(input("Enter Ticket ID to close: "))
            ticket_manager.close_ticket(ticket_id)

        elif choice == "5":
            ticket_id = int(input("Enter Ticket ID to reopen: "))
            ticket_manager.reopen_ticket(ticket_id)

        elif choice == "6":
            ticket_id = int(input("Enter Ticket ID to reopen: "))
            ticket_manager.reopen_ticket(ticket_id)

        elif choice == "7":
            total, resolved, open_tickets = Ticket.TicketStats(ticket_manager.tickets)
            print(f"Total Tickets: {total}")
            print(f"Resolved Tickets: {resolved}")
            print(f"Open Tickets: {open_tickets}")

        elif choice == "8":
            print("Exiting the Help Desk Ticketing System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
