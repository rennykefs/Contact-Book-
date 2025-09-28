#contact book
from operator import truediv
from tkinter.font import names

contact={} # created a dictionary for storage

#Function for contact creation
def create_contact(name, email, phone):
    if name in contact:
        print(f'Contact belonging to {name} already exists')
    else:
        contact[name]={"email":email,"phone":phone}

#Function for contact addition
def add_contact():
    name= input("Enter name: ")
    email= input("Enter email: ")
    phone= input("Enter phone: ")
    create_contact(name,email,phone)# recalling the creating function
# finding contact
def find_contact(name):
    if name in contact:
        print(f"Contact found: Name: {name}, Email: {contact[name]["email"]}, Phone: {contact[name]["phone"]}")
    else:
        print(f'Contact: {name} is not found')

#Update contact
def update_contact(name):
    if name in contact:
        email= input("Enter updated email: ")
        phone= input("Enter updated phone: ")
        contact[name]={"Email": email,"Phone":phone}
        print(f'Contact {name} updated successfully')
    else:
        print(f'Contact{name} not found')

#Delete contact
def delete_contact(name):
    if name in contact:
        del contact[name]
        print(f"Contact {name} deleted successfully ")
    else:
        print(f"Contact {name} not found")

# Menu
def menu():
    while True: #infinite loop enabling continuous interaction.
        print("\n Welcome to contact book")
        print("\n Here is the Menu")
        print("1: Add contact")
        print('2: Find contact')
        print("3: Update contact")
        print("4: Delete Contact")
        print("5: Exit")

        choice=input("Enter option: ")
        if choice=="1":
            add_contact()
        elif choice=="2":
            name= input("Enter the name of the contact you want to find: ")
            find_contact(name)
        elif choice=="3":
            name= input("Enter the name of the contact to update: ")
            update_contact(name)
        elif choice=="4":
            name= input("Enter the name of the contact you want to delete: ")
            delete_contact(name)
        elif choice=="5":
            print("Exiting the contact book")
            break
        else:
            print("Invalid choice")

#start app
menu()


