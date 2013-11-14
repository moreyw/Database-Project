#!/usr/bin/env python

import _mysql

from database import *
from choice import *
from edit import *

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
    
    print "\n{} INFO".format(s[choice]).upper()
    for key in item:
        if 'id' not in key:
            print "{} = {}".format(key, item[key])
    
    edit[s[choice]](item)
    
    return True

if __name__ == "__main__":
    while True:
        if not core_choice():
            break
        print ""
