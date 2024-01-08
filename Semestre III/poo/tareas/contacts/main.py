from controller import AppController
import os

def main():
    app_controller = AppController()
    while True:
        choice = app_controller.app_view.mainMenu()

        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = app_controller.contact_controller.createContact(name, phone, email)
            app_controller.contact_view.displayContact(contact)
            os.system("cls")
            
        elif choice == 2:
            name = input("Enter group name: ")
            group = app_controller.group_controller.createGroup(name)
            app_controller.group_view.displayGroup(group)
    
        elif choice == 3:
            if(app_controller.emptyContacts()):
                print("There are not contacts")
            else:
                if(app_controller.emptyGroup()):
                    print("There are not Groups")
                else:
                    app_controller.viewAllContacts()
                    contact_index = int(input("Enter the index of the contact to add to a group: "))
                    app_controller.viewAllGroups()
                    group_index = int(input("Enter the index of the group to add the contact to: "))
                    try:
                        contact = app_controller.contact_controller.contacts[contact_index]
                        group = app_controller.group_controller.groups[group_index]
                        app_controller.group_controller.addContactToGroup(group, contact)
                        print(f"{contact.name} added to {group.name}")
                    except (IndexError, ValueError):
                        print("Invalid index. Please enter a valid index.")
        elif choice == 4:
            if(app_controller.emptyGroup()):
                print("There are no groups")
            else:
                app_controller.viewAllGroups()
                group_index = int(input("Enter the index of the group to remove a contact from: "))
                try:
                    group = app_controller.group_controller.groups[group_index]
                    if group.contacts:
                        app_controller.viewContactsOfGroup(group)
                        contact_index = int(input("Enter the index of the contact to remove from the group: "))
                        contact = group.contacts[contact_index]
                        app_controller.group_controller.removeContactFromGroup(group, contact)
                        print(f"{contact.name} removed from {group.name}")
                    else:
                        print("No contacts in this group.")
                except (IndexError, ValueError):
                    print("Invalid index. Please enter a valid index.")
        elif choice == 5:
            app_controller.viewAllContacts()
        elif choice == 6:
            app_controller.viewAllGroups()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
