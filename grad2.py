# contact manager app
def add_contact(contacts):
    name=input("Add contact name")
    try:
        phone_number = int(input("Add contact phone number: "))
        contacts[name] = {"name": name, 
                          "phone number": phone_number
                        }
        print(f"Contact {name} was added.")
    except ValueError:
        print("Invalid phone number. Please enter a valid number.")
        
def delete_contact(contacts):
    name=input("Write the name of the contact you want to delete ")
    if name in contacts:
        del contacts[name]            
        print(f"contact {name} was deleted ")
    else:
        print(f"contact {name} isn\'t in your contacts ")
def search_contact(contacts):
    name=input("Write the name of the contact you search for ")
    if name in contacts:
        print(f" the {name} number is : {contacts[name]['phone number'] }")
    else:
        print(f"contact \" {name} \" isn\'t in your contacts")
        
def show_contacts(contacts):
    if  not contacts: #{}
        print("No Contacts are found")
    else:
        for name ,about in contacts.items():
            print(f" {name} : {about['phone number']}")
            
def main():    
 contacts={}
 while True :
       print("Welcome to contacts folder ")
       print("1 . Add contact")
       print("2 . Delete contact")
       print("3 . search contacts")
       print("4. Show contacts")
       print("5. Log out")
       choice=input(" Enter your choice ")
       if choice=="1":
           add_contact(contacts)
       elif choice=="2":
           delete_contact(contacts)
       elif choice=="3":
           search_contact(contacts)
       elif choice=="4":
           show_contacts(contacts)
       elif choice=="5":
            break
       else:
           print("Invalid choice")
if __name__=="__main__":
    main()
