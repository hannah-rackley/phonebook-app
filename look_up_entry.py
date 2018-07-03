def look_up_entry(phonebook):
    name = raw_input("Name: ")
    if name in phonebook:
        return "Found entry for %s: %s" % (name, phonebook[name])
    else:
        return "There is no entry for %s" % name