
from database import *
import choice


def choose_field(fields):
    fields = ["Exit"] + fields

    print "\nFIELDS"
    for i, field in enumerate(fields):
        print "{}: {}".format(i, field)

    selection = None
    while selection not in range(len(fields)):
        try:
            selection = int(raw_input("Edit field (num): "))
            if selection not in range(len(fields)):
                raise ValueError("invalid choice")
        except Exception:
            print "Invalid choice, please try again."

    return fields[selection]

    
def edit_project(project):
    selection = choose_field(["Name"])
    
    if selection == "Name":
        name = raw_input("Enter a new name: ")

        db.query("""

        UPDATE projects SET name='{name}' WHERE
        project_id={id}

        """.format(name=name, id=project["project_id"]))

    db.commit()

def edit_procedure(procedure):
    id = procedure["procedure_id"]
    selection = choose_field(["Name", "Description"])
    
    
    if selection == "Name":
        name = raw_input("Enter a new name: ")

        db.query("""

        UPDATE procedures SET name='{name}' WHERE
        procedure_id={id}

        """.format(name=name, id=id))

    elif selection == "Description":
        description = raw_input("Enter a new description: ")

        db.query("""

        UPDATE procedures SET description='{description}' WHERE
        procedure_id={id}

        """.format(description=description, id=id))
        
    db.commit()

def edit_experiment(experiment):
    id = experiment["experiment_id"]
    selection = choose_field(["Name", "Project", "Procedure"])

    if selection == "Name":
        name = raw_input("Enter a new name: ")

        db.query("""

        UPDATE procedures SET name='{name}' WHERE
        experiment_id={id}

        """.format(name=name, id=id))
        
    elif selection == "Project":
        new_project = choice.make_choice("projects",
                                         "SELECT name, project_id FROM projects")
            
        db.query("""
        
        UPDATE experiments SET project_id='{project_id}' WHERE
        experiment_id={id}
            
        """.format(id=id, project_id=new_project["project_id"]))

#    elif selection == "Procedure":
        
    
