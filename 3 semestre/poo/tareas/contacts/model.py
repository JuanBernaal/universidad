class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Group:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def addContact(self, contact):
        if(contact not in self.contacts):
            self.contacts.append(contact)

    def removeContact(self, contact):
        self.contacts.remove(contact)
