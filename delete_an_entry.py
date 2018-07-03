def delete_an_entry(phonebook):
    name = raw_input("Name: ")
    if name in phonebook:
        del phonebook[name]
        return "Deleted entry for %s" % name
    else:
        return "There is no entry for %s" % name
