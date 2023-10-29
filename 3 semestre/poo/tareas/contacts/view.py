class ContactView:
    def displayContact(self, contact):
        print(f"Contact: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print()

class GroupView:
    def displayGroup(self, group):
        print(f"Group name: {group.name}")
        if group.contacts:
            print("Contacts in group:")
            for contact in group.contacts:
                print(f"  - {contact.name}")
        else:
            print("No contacts in this group.")
        print()

class View:
    def mainMenu(self):
        print("1. Create Contact")
        print("2. Create Group")
        print("3. Add Contact to Group")
        print("4. Remove Contact from Group")
        print("5. View All Contacts")
        print("6. View All Groups")
        print("7. Exit")
        return int(input("Enter your choice: "))
