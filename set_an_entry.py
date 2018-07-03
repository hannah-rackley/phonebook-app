def set_an_entry(phonebook):
    name = raw_input("Name: ")
    phone_number = raw_input("Enter phone number formatted like this ###-###-####: ")
    phonebook[name] = phone_number
    return "Entry stored for %s" % name