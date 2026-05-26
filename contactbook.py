contacts={}

def add_contact():
    name=input("Enter the contact's name : ")
    phone_no=input("Enter the phone number of contact : ")
    contacts[name]=phone_no


def search_contact():
    i=input("enter the name u want to search: ")
    if i in contacts:
        print(contacts[i])
    else:
        print("Contact Not found")


def show_all():
    for name, number in contacts.items():
        print(name, ":", number)


while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Show all")
    print("4. Quit")

    choice=input("choose: ")
    

    if choice=="1":
        add_contact()

    if choice=="2":
        search_contact()

    if choice=="3":
        show_all()

    elif choice=="4":
        break


