
from database import *


def choose_field(fields):
    fields = ["Exit"] + fields

    print "\nFIELDS"
    for i, field in enumerate(fields):
        print "{}: {}".format(i, field)

    choice = None
    while choice not in range(len(fields)):
        try:
            choice = int(raw_input("Edit field (num): "))
            if choice not in range(len(fields)):
                raise ValueError("invalid choice")
        except Exception:
            print "Invalid choice, please try again."

    return fields[choice]

    
def edit_project(project):
    choice = choose_field(["Name"])
    
    if choice == "Name":
        name = raw_input("Enter a new name: ")

        db.query("""

        UPDATE projects SET name='{name}' WHERE
        project_id={id}

        """.format(name=name, id=project["project_id"]))

    db.commit()

def edit_procedure(procedure):
    id = procedure["procedure_id"]
    choice = choose_field(["Name", "Description"])
    
    if choice == "Name":
        name = raw_input("Enter a new name: ")

        db.query("""

        UPDATE procedures SET name='{name}' WHERE
        procedure_id={id}

        """.format(name=name, id=id))

    elif choice == "Description":
        description = raw_input("Enter a new description: ")

        db.query("""

        UPDATE procedures SET description='{description}' WHERE
        procedure_id={id}

        """.format(description=description, id=id))
        
    db.commit()
