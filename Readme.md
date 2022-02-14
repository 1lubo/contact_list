
# Contact List

## Contact List program that can persistently store a list of a user’s contacts.

https://www.programmingexpert.io/projects/contact-list

![prompt](/assets/prompt.png)



Each contact in the contact list requires a first name and last name but all other fields are optional. The optional fields that you should prompt the user to input are the following:

    -Mobile Phone Number
    -Home Phone Number
    -Email Address
    -Address

Contacts in the contact list are unique, meaning no two contacts can have both the same first and last names. However, contacts can share a first name or a last name, just not both.

Your program should work similarly to a command line interface, where you constantly ask the user to enter one of the following commands:

    **-add**: Adds a contact to the contact list.
    **-delete**: Deletes a contact from the contact list using it's first and last name.
    **-list**: Lists all the contacts in alphabetical order by first name.
    **-search**: Searches for contacts by their first and last name.
    **-q**: Quits the program and saves all of the current contacts.

When adding contacts ensure that all phone numbers that are entered are valid. For this project a phone number is valid if it is 10 digits and only contains numbers. Do the same with the email (a helper function is provided that verifies emails for you).

When searching for contacts simply display all contacts that contain the strings used to search for first and last names. For example, if your search strings are `first_name = "t"`and `last_name = "r"` then you should display the following names:

    -Stan Right
    -Tim Archer
    -Thomas Rong

All names that contain a `t` in the first name and a `r` in the last name are displayed. You should also display all of the search results in alphabetical order.

