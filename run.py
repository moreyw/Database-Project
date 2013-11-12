#!/usr/bin/env python

import _mysql

from create import *
from database import *

call = {
    'projects' : new_project,
    'procedures' : new_procedure
}

def choose_existing(statement):
    db.query(statement)
    r=db.store_result()

    #get all rows as dictionaries
    rows = r.fetch_row(maxrows=0, how=1)
    size = len(rows)

    if not size:
        return None
    
    for num, row in enumerate(rows):
        print "{}: {}".format(num, row["name"])

    choice = None
    while choice not in range(size):
        try:
            choice = int(raw_input("Select an existing value: "))
            if choice not in range(size):
                raise ValueError("invalid choice")
                
        except Exception:
            print "Invalid choice, please try again."

    return rows[choice]

def create_new(value_type):
    call[value_type]()

def make_choice(name, statement, new_option=True):
    choice = None
    if new_option:
        while choice not in range(1, 3):
            try:
                choice = int(raw_input("Choose existing {}[1] or create new[2]: ".format(name)))
                if choice not in range(1, 3):
                    raise ValueError("invalid choice")
                    
            except Exception:
                print "Invalid choice, please try again."
    else:
        choice = 1

    if choice == 1:
        selected = choose_existing(statement)
        if selected:
            return selected
        else:
            choice = 2

    if choice == 2:
        return create_new(name)

def core_choice():
    s = ( "exit",
          "projects",
          "procedures",
          "experiments",
          "reagents",
          "equipment",
          "specimens")
    for index, item in enumerate(s):
        print "{}: {}".format(index, item)

    choice = None
    while choice not in range(len(s)):
        try:
            choice = raw_input("=>")
            if choice == "":
                continue
            else:
                choice = int(choice)
                
            if choice == 0:
                return None
            elif choice not in range(len(s)):
                raise ValueError("invalid choice")
        except Exception:
            print "Invalid choice, please try again."

    item = make_choice(s[choice], "SELECT * FROM {}".format(s[choice]))
    
    return True

if __name__ == "__main__":
    while True:
        if not core_choice():
            break
        print ""
