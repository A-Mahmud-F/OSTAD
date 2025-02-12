def add_contact(contacts):
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")

    # Check for duplicate phone number
    for contact in contacts:
        if contact["phone"] == phone:
            print("Error: Phone number already exists.")
            return

    contacts.append({
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    })
    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contacts ---")
        for contact in contacts:
            print(
                f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")


def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to remove: ")
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact removed successfully!")
            return
    print("Error: Contact not found.")


def search_contact(contacts):
    search_term = input("Enter name, email, or phone number to search: ")
    results = []
    for contact in contacts:
        if (search_term.lower() in contact["name"].lower() or
                search_term.lower() in contact["email"].lower() or
                search_term == contact["phone"]):
            results.append(contact)

    if results:
        print("\n--- Search Results ---")
        for result in results:
            print(
                f"Name: {result['name']}, Email: {result['email']}, Phone: {result['phone']}, Address: {result['address']}")
    else:
        print("No matching contacts found.")