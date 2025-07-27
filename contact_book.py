import json
import os

FILE_NAME = "contacts.json"


def load_contact():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    else:
        return {}


def save_contact(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)


def show_menu():
    print("\n📖 Contact Book Menu:")
    print("1. Add Contact")
    print("2. View All Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def view_contact():
    contacts = load_contact()
    if not contacts:
        print("No Contact Found ")
    else:
        for name, info in contacts.items():
            print("\n🙂Name: ", name)
            print("📞Phone: ", info["phone"])
            print("📧Email: ", info["email"])
            print("-" * 20)


def add_contact():
    contacts = load_contact()
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email (Optional): ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    save_contact(contacts)
    print(f"✅ {name} added Successfully!")


def seach_contact():
    contacts = load_contact()
    name = input("Enter the name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"\n🔎 Found the contact for {name}")
        print(f"📞 Phone: {info['phone']}")
        print(f"📧 Email: {info['email']}")
    else:
        print("❌ Contact Not Found")


def delete_contact():
    contacts = load_contact()
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contact(contacts)
        print(f"🗑️ {name} deleted Successfully")
    else:
        print("❌ Contact Not Found")


show_menu()
while True:
    choice = input("Enter your choice (1-5): ")

    if(choice == '1'):
        add_contact()
    elif(choice == '2'):
        view_contact()
    elif(choice == '3'):
        seach_contact()
    elif(choice == '4'):
        delete_contact()
    elif(choice == '5'):
        break
else:
        print("Invalid Choice! Please enter a number between 1 to 5")
