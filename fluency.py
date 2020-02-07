import re

def tripled(lst):
    return [ num * 3 for num in lst]

def only_negative(lst):
    return [num < 0 for num in lst]
 
def total(lst):
     return sum(lst)

def stripped_strings(lst):
    return [re.sub('\W', '', string) for string in lst]

def find_lovely(lst):
    if not lst.index('lovely'):
        return -1
    return lst.index('lovely')
    
def valid_contacts(lst):
    return [contact for contact in lst if len(contact['phone_number']) == 10]

def contact_names(lst):
    return [ contact['name'] for contact in lst]