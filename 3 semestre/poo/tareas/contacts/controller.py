from model import Contact, Group
from view import ContactView, GroupView, View

class ContactController:
    def __init__(self):
        self.contacts = []

    def createContact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        return contact

class GroupController:
    def __init__(self):
        self.groups = []

    def createGroup(self, name):
        group = Group(name)
        self.groups.append(group)
        return group

    def addContactToGroup(self, group, contact):
        group.addContact(contact)

    def removeContactFromGroup(self, group, contact):
        group.removeContact(contact)

class AppController:
    def __init__(self):
        self.contact_controller = ContactController()
        self.group_controller = GroupController()
        self.contact_view = ContactView()
        self.group_view = GroupView()
        self.app_view = View()

    def viewAllContacts(self):
        i = 0
        for contact in self.contact_controller.contacts:
            print(f"Contact #{i}")
            self.contact_view.displayContact(contact)
            i += 1

    def viewContactsOfGroup(self, group):
        i = 0
        for contact in group.contacts:
            print(f"Contact #{i}")
            self.contact_view.displayContact(contact)
            i += 1

    def viewAllGroups(self):
        i = 0
        for group in self.group_controller.groups:
            print(f"Group #{i}")
            self.group_view.displayGroup(group)
            i += 1

    def emptyGroup(self):
        ans = True
        if(len(self.group_controller.groups) == 0):
            ans = True
        else:
            ans = False
        return ans

    def emptyContacts(self):
        ans = True
        if(len(self.contact_controller.contacts) == 0):
            ans = True
        else:
            ans = False
        return ans