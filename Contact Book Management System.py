from contact_manager import add_contact, view_contacts, remove_contact, search_contact
from file_handler import load_contacts, save_contacts


def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            remove_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()