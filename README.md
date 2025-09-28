# 📒 Contact Book Application (Python)

## Introduction

It allows users to **create, read, update, and delete (CRUD)** contact information such as name, email, and phone number.


## 💻 Features
- ➕ Add a new contact  
- 🔍 Find an existing contact  
- ✏️ Update contact information  
- 🗑️ Delete a contact  
- 📜 Menu-driven system with continuous interaction  

---

## 🧑‍💻 The Script
```python
# contact book

contact = {}  # dictionary for storage

# Function for contact creation
def create_contact(name, email, phone):
    if name in contact:
        print(f'Contact belonging to {name} already exists')
    else:
        contact[name] = {"email": email, "phone": phone}

# Function for contact addition
def add_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    create_contact(name, email, phone)

# Finding contact
def find_contact(name):
    if name in contact:
        print(f"Contact found: Name: {name}, Email: {contact[name]['email']}, Phone: {contact[name]['phone']}")
    else:
        print(f'Contact {name} not found')
# Menu
def menu():
    while True:
        print("\nWelcome to Contact Book")
        print("\nHere is the Menu")
        print("1: Add contact")
        print("2: Find contact")
        print("3: Update contact")
        print("4: Delete Contact")
        print("5: Exit")

        choice = input("Enter option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            name = input("Enter the name of the contact you want to find: ")
            find_contact(name)
        elif choice == "3":
            name = input("Enter the name of the contact to update: ")
            update_contact(name)
        elif choice == "4":
            name = input("Enter the name of the contact you want to delete: ")
            delete_contact(name)
        elif choice == "5":
            print("Exiting the contact book")
            break
        else:
            print("Invalid choice")

# Start app
menu()

```
---

## 📚 What I Learned

Using dictionaries for structured data storage

Creating and calling functions

Using if / elif / else logic

Implementing loops for continuous user interaction

Building a menu-driven Python application

