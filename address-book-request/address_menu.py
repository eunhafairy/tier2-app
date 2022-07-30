from email.mime import base
import time
import os
from urllib import response
from address_client_api import AddressClientApi

global address_contact
address_contact = None
addressClientApi = AddressClientApi()


def requirement_check(data):
    if data == "":
        print("This Field is Required")
        return False
    else:
        return True



def add_contact():
    print("\nAdd New Address")
    while True:
        name = input("Name (Required): ")
        if requirement_check(name) == True:
            break
    while True:
        address = input("Address (Required): ")
        if requirement_check(address) == True:
            break
    contact = input("Enter Contact: ")
    email = input("Enter Email: ")
    new_entry = {
        "name":name,
        "address":address,
        "contact":contact,
        "email":email
    }
    
    addressClientApi.add_new_address_contacts(new_entry)
    print("\nSuccessfully added!")


def display_search_result(result):
  
    index = 1
    print("** Address Book **".rjust(53)+"\n"+"No.".rjust(5)+"|"+"Name".rjust(20)+"|"+"Address".rjust(20)+ "|"+"Contact".rjust(20)+"|"+"Email".rjust(20)+"")
    for entry in result:
        print("{}|{}|{}|{}|{}".format(
            str(index).rjust(5),
            entry.get("name").rjust(20),
            entry.get("address").rjust(20),
            str(entry.get("contact")).rjust(20),
            entry.get("email").rjust(20)
            ))
        index = index + 1


def search_address_contact(operation):
    name = input("Enter Name: ")
    result = addressClientApi.find_address_contact(name)
    record_for_edit = None
    
    if len(result) > 1:
        
        display_search_result(result)
        while True:
            try:
                id = int(input("\nEnter Address ID to {} [1-{}]: ".format(operation,len(result))))
                if id > len(result):
                    print("Invalid Selection, Please Try Again")
                else:
                    record_for_edit = result[id-1]
                    break
            except ValueError:
                print("Invalid input")

    elif len(result) == 1:
        display_search_result(result)
        record_for_edit = result[0]
    else:
        print("Address not found")

    return record_for_edit


def update_contact():
    print("\n**Update Address**\n")
    print("Search Address")
    display_edit_screen(search_address_contact("edit"))

def delete_contact():
    print("\n**Delete Address**\n")
    print("Search Address")
    result = search_address_contact("delete")
    if result != None:
        while True:
            response = input("Delete Address (Y/N)?")
            if response.lower() == "y":
                addressClientApi.delete_address_contact(result)
                print("Successfully deleted. \n")
                break
            elif response.lower() == "n":
                input("\nUser cancelled, press enter key to quit")
                break
            else:
                print("Invalid Selection")


def display_edit_screen(record_for_edit):
    
    clear_screen()
    if record_for_edit != None:
        clear_screen()
        get_user_input = lambda input, default : input if input.strip() != "" else default
        name = record_for_edit.get("name")
        address =  record_for_edit.get("address")
        contact =  record_for_edit.get("contact")
        email =  record_for_edit.get("email")
        print("** EDIT ADDRESS CONTACT **")
        name = get_user_input(input("New Name [{}]: ".format(name)),name)
        address = get_user_input(input("New Address [{}]: ".format(address)),address)
        contact = get_user_input(input("New Contact [{}]: ".format(contact)),contact)
        email = get_user_input(input("New Email [{}]: ".format(email)),email)

        record_for_edit["name"] = name
        record_for_edit["address"] = address
        record_for_edit["contact"] = contact
        record_for_edit["email"] = email
        addressClientApi.update_address_contact(record_for_edit)
        print("Successfully Updated. \n")



def clear_screen():
    os.system("cls")

def transaction_selection():
    while True:
        selection = input("\nGo back to main menu again? [Y/N]: ")
        if selection.lower() == "y":
            clear_screen()
            return True
        elif selection.lower() == "n":
            clear_screen()
            print("Thank you for using the app.")
            return False


def display_menu():
    clear_screen()
    while True:
        print("\nAddress Book")
        print("\t1. Display Address/es")
        print("\t2. Add New Address")
        print("\t3. Update Address")
        print("\t4. Delete Address")
        selection = input("\nEnter Selection: ")

        if selection == "1":
            clear_screen()
            print("Loading...")
            time.sleep(1)
            clear_screen()
            display_search_result(addressClientApi.get_address_contacts().get("details"))
            if transaction_selection() == False:
                break
        elif selection == "2":
            clear_screen()
            add_contact()
            if transaction_selection() == False:
                break
        elif selection == "3":
            clear_screen()
            update_contact()
            if transaction_selection() == False:
                break
        elif selection == "4":
            clear_screen()
            delete_contact()
            if transaction_selection() == False:
                break
        else:
            print("Enter valid input")

display_menu()    
