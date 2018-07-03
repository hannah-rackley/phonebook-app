def list_all_entries(phonebook):
    string = ""
    for name in phonebook:
        string += "Found entry for %s: %s\n" % (name, phonebook[name])
    return string