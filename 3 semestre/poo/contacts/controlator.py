from model import ContactMethods, ContactModel
from view import ContactView


class ContactController:
    def __init__(self):
        self.model = ContactMethods()
        self.view = ContactView()

    def add_new_contact(self, name, phone, email):
        contact = ContactModel(name, phone, email)
        self.model.add_new_contact(contact)

    def display_all_contacts(self):
        contacts_list = self.model.get_all_contacts()
        self.view.display_all_contacts(contacts_list)


if __name__ == "__main__":
    controller = ContactController()

    while True:
        print("1. Add New Contact")
        print("2. Display All Contacts")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            controller.add_new_contact(name, phone, email)
        elif choice == "2":
            controller.display_all_contacts()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Update please