# Contact book 

contacts = {}  # Dictionary to store contacts

def add_contact():
    print("\nEnter contact details:")
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email address: ")
    address = input("Address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"\nContact '{name}' added successfully!")

def view_contact_list():
    if contacts:
        print("\nList of Contacts:")
        for name, contact_info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {contact_info['phone']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            print("-" * 20)
    else:
        print("\nContact list is empty.")

def search_contact():
    if contacts:
        search_term = input("\nEnter name or phone number to search: ").strip().lower()
        found = False
        for name, contact_info in contacts.items():
            if search_term in name.lower() or search_term == contact_info['phone']:
                print("\nContact found:")
                print(f"Name: {name}")
                print(f"Phone: {contact_info['phone']}")
                print(f"Email: {contact_info['email']}")
                print(f"Address: {contact_info['address']}")
                found = True
        if not found:
            print("No matching contact found.")
    else:
        print("\nContact list is empty.")

def update_contact():
    if contacts:
        name = input("\nEnter name of contact to update: ")
        if name in contacts:
            print(f"\nCurrent details for '{name}':")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
            print(f"Address: {contacts[name]['address']}")
            choice = input("\nWhat do you want to update (phone/email/address)? ").strip().lower()
            if choice == 'phone':
                contacts[name]['phone'] = input("Enter new phone number: ")
            elif choice == 'email':
                contacts[name]['email'] = input("Enter new email address: ")
            elif choice == 'address':
                contacts[name]['address'] = input("Enter new address: ")
            else:
                print("Invalid choice.")
            print(f"\nContact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")
    else:
        print("\nContact list is empty.")

def delete_contact():
    if contacts:
        name = input("\nEnter name of contact to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"\nContact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")
    else:
        print("\nContact list is empty.")

# Main menu loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
