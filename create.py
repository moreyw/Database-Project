
from database import *

def new_project():
    print("Creating new project")
    name = raw_input("New project name: ")

    db.query("INSERT INTO projects (project_id, name) VALUES (NULL, '{}')".format(
        name))

    print "New project created"


def new_procedure():
    print("Creating new procedure")
    name = raw_input("New procedure name: ")
    description = raw_input("Briefly describe the procedure: ")

    db.query("""
    
    INSERT INTO procedures (procedure_id, name, description)
    VALUES (NULL, '{}', '{}')
    """.format(name, description))

    print "New procedure created"
    

