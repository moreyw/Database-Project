
from database import *

def new_project():
    print("Creating new project")
    name = raw_input("New project name: ")

    db.query("INSERT INTO projects (project_id, name) VALUES (NULL, '{}')".format(
        name))

    print "New project created"
    

