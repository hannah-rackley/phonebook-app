#Functions to be called in main function:
import print_header
import look_up_entry
import set_an_entry
import delete_an_entry
import list_all_entries

def stop():
    print "Bye"

#Phonebooks that can be called within the function.
phonebook1 = {
    "John": "000-000-0000",
    "Jacob": "100-100-1100",
    "Jingle": "200-200-2200"
}

phonebook2 = {
    "May": "000-000-0000",
    "June": "100-100-1100",
    "July": "200-200-2200"
}
#Main
def enter_phonebook(phonebook):
    choice = print_header.print_header(phonebook)
    options = {
        "1": look_up_entry.look_up_entry,
        "2": set_an_entry.set_an_entry,
        "3": delete_an_entry.delete_an_entry,
        "4": list_all_entries.list_all_entries
    }
    while choice != "5":
        if choice in options:
            print options[choice](phonebook)
            choice = print_header.print_header(phonebook)
        else:
            print "Invalid input, try again"
            choice = print_header.print_header(phonebook)
    return stop()
    
enter_phonebook(phonebook1)