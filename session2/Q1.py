FILE_NAME = "contacts.txt"


def load_contacts():
    contacts = {}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass

    return contacts


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")


def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Display All Contacts")
    print("5. Exit")


def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = phone
        print("Contact added successfully.")


def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def search_contact(contacts):
    name = input("Enter contact name to search: ").strip()

    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print("Contact not found.")


def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- All Contacts ---")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")


def main():
    contacts = load_contacts()
    print("Contacts loaded successfully.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            delete_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            display_contacts(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
