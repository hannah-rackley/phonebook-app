import print_header
import look_up_entry
import set_an_entry
import delete_an_entry
import list_all_entries

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

def stop():
    print "Bye"

def enter_phonebook(phonebook):
    choice = print_header.print_header(phonebook)
    
    while choice != "5":
        if choice == "1":
            print look_up_entry.look_up_entry(phonebook)
        elif choice == "2":
            print set_an_entry.set_an_entry(phonebook)
        elif choice == "3":
            print delete_an_entry.delete_an_entry(phonebook)
        elif choice == "4":
            print list_all_entries.list_all_entries(phonebook)
        else:
            print "Invalid entry"
        choice = print_header.print_header(phonebook)

    return stop()


enter_phonebook(phonebook2)






