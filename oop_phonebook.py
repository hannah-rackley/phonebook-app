# #Functions to be called in main function:
# import print_header
# import look_up_entry
# import set_an_entry
# import delete_an_entry
# import list_all_entries

# def stop():
#     print "Bye"

#Phonebook Notes
class App(object):

    def __init__(self):
        self.phonebook = Phonebook()

    def create_new_contact(self):
        name = raw_input("Please enter name: ")
        number = raw_input("Please enter number: ")
        contact = Contact({
            'name': name,
            'number': number
        })
        return self.phonebook.add(contact)
    
    def print_phonebook_options(self):
        print 
        print "Electronic Phone Book"
        print "=================="
        print "1. Look up an entry"
        print "2. Set an entry"
        print "3. Delete an entry"
        print "4. List all entries"
        print "5. Quit" 
        choice = raw_input("What do you want to do (1-5)? ")
        return choice
    
    def start(self):
        keep_running = True
        while keep_running:
            choice = self.print_phonebook_options()
            if choice == "1":
                contact = raw_input("Please enter the name you are trying to look up: ")
                print self.phonebook.lookup_by_name(contact)
            elif choice == "2":
                print self.create_new_contact()
            elif choice == "3":
                contact = raw_input("Please enter the name of the contact you want to remove: ")
                print self.phonebook.remove(contact)
            elif choice == "4":
                print self.phonebook.list_as_sorted_list()
            elif choice == "5":
                keep_running = False
                print "Bye"
            else:
                print "That is not a valid input, please try again."


    def __repr__(self):
        return "Name: %s and Number: %s" % (self.contact['name'], self.contact['number'])

class Contact(object):
    def __init__(self, params):
        self.attributes = params
    
    def get_attr(self, attr):
        if attr in self.attributes:
            return self.attributes[attr]
        else:
            return ''

    def get_name(self):
        return self.get_attr('name')
    
    def get_number(self):
        return self.get_attr('number')
    
    def as_string(self):
        return "%s : %s" % (self.get_name(), self.get_number())

class Phonebook(object):
    #stores lists of contacts
    def __init__(self):
        self.contacts = []

    def lookup_by_name(self, name):
        for contact in self.contacts:
            if name == contact.get_name():
                return "%s's number is: %s" % (contact.get_name(), contact.get_number())
        
        return "%s is not in this phonebook." % name

    def add(self, contact):
        if contact in self.contacts:
            return "%s is already in the phonebook. The associated number is: %s" % (contact.get_name(), contact.get_number())
        else:
            self.contacts.append(contact)
            return "%s has been added to the phonebook" % contact.get_name()
    
    def remove(self, name):
        for contact in self.contacts:
            if name == contact.get_name():
                self.contacts.remove(contact)
                return "%s's entry has been deleted." % name
        else:
            return "%s is not in this phonebook" % name
    
    def list_as_sorted_list(self):
        contact_lst = []
        for contact in self.contacts:
            contact_lst.append(contact.as_string())
        sorted_list = sorted(contact_lst)
        string = ''
        for person in sorted_list:
            string += (person + '\n')
        return string

app = App()

app.start()


