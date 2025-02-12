import csv

def load_contacts():
    contacts = []
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass  # File doesn't exist yet
    return contacts

def save_contacts(contacts):
    with open("contacts.csv", "w", newline="") as file:
        fieldnames = ["name", "email", "phone", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)