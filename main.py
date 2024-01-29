import os
from contact import Contact

# Function to load contacts from the file
def load_contacts():
    contacts = []
    if os.path.exists('data/contacts.txt'):
        with open('data/contacts.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name, phone, email = parts
                    contacts.append(Contact(name, phone, email))
    return contacts

# Function to save contacts to the file
def save_contacts(contacts):
    with open('data/contacts.txt', 'w') as file:
        for contact in contacts:
            contact_dict = contact.to_dict()
            file.write(f"{contact_dict['name']},{contact_dict['phone']},{contact_dict['email']}\n")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    contact = Contact(name, phone, email)
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to list all contacts
def list_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact}")

# Function to delete a contact
def delete_contact(contacts, index):
    if 1 <= index <= len(contacts):
        deleted_contact = contacts.pop(index - 1)
        save_contacts(contacts)
        print(f"Contact deleted: {deleted_contact}")
    else:
        print("Invalid contact index")

# Main program loop
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Delete Contact")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            list_contacts(contacts)
        elif choice == '3':
            index = int(input("Enter the index of the contact to delete: "))
            delete_contact(contacts, index)
        elif choice == '4':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
