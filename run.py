#!/usr/bin/env python

import _mysql

from database import *
from choice import *
from edit import *
from report import generate_report

def core_choice():
    s = ( "exit",
          "projects",
          "procedures",
          "experiments",
          "reagents",
          "equipment",
          "specimens",
          "generate report")

    print "Edit or create new: "
    
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

    if s[choice] == "generate report":
        generate_report()
        return True
        
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
