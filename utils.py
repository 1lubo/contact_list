from curses.ascii import isdigit
import json


def check_email(email):

    if '@' not in email:
        return False  # not an email if @ is missing

    index = email.index('@')
    domain = email[index + 1:]

    if index == 0:  # not an email if it starts with @
        return False

    if '.' not in domain:  # not an email if there's no domain name
        return False

    return True


def check_phone_number(phone_number):
    # remove '-' from number
    format_number = phone_number.replace('-', '')

    # check if characters are digits
    for num in format_number:
        if not isdigit(num):
            return False
    if len(format_number) != 10:
        return False

    return True


def delete_contact(contact_list):

    message_result = 'No contact with this name exists.'
    # ask for input
    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    # iterate through contacts to find contact
    for ind, contact in enumerate(contact_list.get('contacts')):
        # if contact is found ask to delete
        if first_name == contact.get("first") and last_name == contact.get('last'):
            delete = input(
                "Are you sure you would like to delete this contact (y/n)? ")
            # if answer is yes delete contact
            if delete.lower() == 'y':
                contact_list.get('contacts').pop(ind)

                message_result = 'Contact deleted!'
                break
            else:
                message_result = 'Contact not deleted!'
                break

    print(message_result)


def add_contact(contact_list):
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    mobile = input("Mobile Phone Number: ")
    home = input("Home Phone Number: ")
    email = input("Email Address: ")
    address = input("Address: ")
    message_success = 'Contact Added!'
    message_fail = 'You entered invalid information, this contact was not added.'
    message_detail = None

    # get list of people with same first and last names in contacts
    contact_in_list = len(list(filter(lambda x: first_name.lower() in x.get(
        'first').lower() and last_name.lower() in x.get('last').lower(), contact_list.get('contacts'))))

    # if the list has any items it means there already is a person with the same first and last name
    if contact_in_list > 0:
        message_detail = 'A contact with this name already exists.'
        print(message_detail + '\n' + message_fail)
        return False

    # if a mobile phone number has been entered check the number
    if len(mobile) > 0:
        if not check_phone_number(mobile):
            message_detail = 'Invalid mobile phone number.'
            print(message_detail + '\n' + message_fail)
            return False

    # if a home phone number has been entered check the number
    if len(home) > 0:
        if not check_phone_number(home):
            message_detail = 'Invalid home phone number.'
            print(message_detail + '\n' + message_fail)
            return False

    if len(email) > 0:
        if not check_email(email):
            message_detail = 'Invalid email address.'
            print(message_detail + '\n' + message_fail)
            return False

    # if all data valid create a new contact and add it to list of contacts
    new_contact = {
        "first": first_name,
        "last": last_name,
        "cell": mobile,
        "home": home,
        "email": email,
        "address": address
    }
    contact_list.get('contacts').append(new_contact)
    print(message_success)


def print_contacts(list_of_contacts):

    contact_number = 1  # variable to keep track of the number of listed out contacts
    if len(list_of_contacts) < 1:
        print('Contact list is empty')
        return False

    for contact in list_of_contacts:  # iterate through contacts
        print(f"{contact_number}. {contact.get('first')} {contact.get('last')}")
        for key, value in contact.items():  # print out contact details if the value is not blank
            if value != '' and key != 'first' and key != 'last':
                print(f"\t {key}: {value}")
        contact_number += 1


def search_contacts(contact_list):
    # get input for first name search
    first_name_filer = input("First name: ").lower()
    # get input for last name search
    last_name_filter = input("Last name: ").lower()

    # create a filtered list. Check each contacts first and last name.
    filtered_list = list(filter(lambda x: first_name_filer in x.get(
        'first').lower() and last_name_filter in x.get('last').lower(), contact_list.get('contacts')))

    # print how many contacts were found
    if len(filtered_list) < 1:
        print('No contact with this name exists.')
    else:
        # if 1 or more contacts found print contacts sorted by first name
        print(f"Found {len(filtered_list)} matching contacts")
        print_contacts(sorted(filtered_list, key=lambda x: x.get('first')))


def list_contacts(contact_list):
    sorted_contact_list = sorted(contact_list.get('contacts'),
                                 key=lambda x: x.get('first'))  # sort contacts by first name

    print_contacts(sorted_contact_list)
