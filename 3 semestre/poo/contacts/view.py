class ContactView:
    def __init__(self):
        print("Contacts List")

    def add_new_contact(self):
        print("Add a new contact")

    def display_all_contacts(self, contacts_list):
        print("The contacts listed are:")
        for contact in contacts_list:
            print(
                f"Contact name: {contact.name}. Phone number: {contact.phone}. Email: {contact.email}"
            )
