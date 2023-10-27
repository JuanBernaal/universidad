class ContactModel:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactMethods:
    def __init__(self):
        self.contactsList = list()

    def get_all_contacts(self):
        return self.contactsList

    def add_new_contact(self, contact):
        self.contactsList.append(contact)
        print("New contact added")
