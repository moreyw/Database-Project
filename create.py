
from database import *
import choice

def new_project():
    print("Creating new project")
    name = raw_input("New project name: ")

    db.query("INSERT INTO projects (project_id, name) VALUES (NULL, '{}')".format(
        name))

    print "New project created"

    db.query("SELECT * FROM projects WHERE project_id = {}".format(db.insert_id()))
    r = db.store_result()
    return r.fetch_row(how=1)[0]


def new_procedure():
    print("Creating new procedure")
    name = raw_input("New procedure name: ")
    description = raw_input("Briefly describe the procedure: ")

    db.query("""
    
    INSERT INTO procedures (procedure_id, name, description)
    VALUES (NULL, '{}', '{}')
    """.format(name, description))

    print "New procedure created"
    
    db.query("SELECT * FROM procedures WHERE procedure_id = {}".format(db.insert_id()))
    r = db.store_result()
    return r.fetch_row(how=1)[0]

def new_experiment():
    print("Creating new experiment")
    name = raw_input("New experiment name: ")

    print("Choose procedure for the experiment.")
    procedure = choice.make_choice("procedures",
                            "SELECT name, procedure_id FROM procedures")

    print("Choose the project the experiment is part of.")
    project = choice.make_choice("projects",
                                 "SELECT name, project_id FROM projects")
    
    
    db.query("""
    
    INSERT INTO experiments (experiment_id, project_id, procedure_id, name)
    VALUES (NULL, '{}', '{}', '{}')
    """.format(project["project_id"], procedure["procedure_id"], name))

    print "New experiment created"
    
    db.query("SELECT * FROM experiments WHERE experiment_id = {}".format(db.insert_id()))
    r = db.store_result()
    return r.fetch_row(how=1)[0]

def new_reagent():
    print("Creating new reagent")
    name = raw_input("New reagent name: ")
    status = raw_input("Reagent status: ")
    location = raw_input("Reagent location: ")

    db.query("""
    
    INSERT INTO reagents (reagent_id, name, status, location)
    VALUES (NULL, '{}', '{}', '{}')
    """.format(name, status, location))

    print "New reagent created"
    
    db.query("SELECT * FROM reagents WHERE reagent_id = {}".format(db.insert_id()))
    r = db.store_result()
    return r.fetch_row(how=1)[0]
