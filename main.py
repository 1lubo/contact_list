import utils
from os.path import exists
import json

quit = False

file_name = "contacts.json"

header = {"contacts": []}

# if file does not exist create a new file

if not exists(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(header, file, ensure_ascii=False, indent=4)

with open(file_name, 'r') as file:
    contact_object = json.load(file)

if __name__ == '__main__':
    print(
        '''
Welcome to your contact list!
The following is a list of useable commands:      
"add": Adds a contact.
"delete": Deletes a contact.
"list": Lists all contacts.
"search": Searches for a contact by name.
"q": Quits the program and saves the contact list.
        '''
    )


while quit != True:
    user_input = input('Type a command: ')
    user_input.lower()

    if user_input == 'add' or user_input == 'a':
        utils.add_contact(contact_object)

    if user_input == 'delete' or user_input == 'd':
        utils.delete_contact(contact_object)

    if user_input == 'list' or user_input == 'l':
        utils.list_contacts(contact_object)

    if user_input == 'search' or user_input == 's':
        utils.search_contacts(contact_object)

    if user_input == 'q':
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(contact_object, file, ensure_ascii=False, indent=4)
        print('Contacts were saved successfully.')
        quit = True
