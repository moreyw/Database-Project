
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

    elif selection == "Procedure":
        new_procedure = choice.make_choice("procedures", 
                                            "SELECT name, procedure_id FROM procedures")

        db.query("""

            UPDATE experiments SET procedure_id='{procedure_id}' WHERE 
            experiment_id={id}

            """.format(id=id, procedure_id=new_procedure["procedure_id"]))

def edit_reagent(reagent):
    id = reagent["reagent_id"]
    selection = choose_field(["Name", "Status", "Location"])

    if selection == "Name":
        name = raw_input("Enter a new name: ")

        db.query("""

            UPDATE reagents SET name='{name}' WHERE
            reagent_id={id}

            """.format(name=name, id=id))
    
    elif selection == "Status":
        status = raw_input("Enter new status: ")

        db.query("""

            UPDATE reagents SET status='{status}' WHERE
            reagent_id={id}

            """.format(status=status, id=id))

    elif selection == "Location":
        location = raw_input("Enter new location: ")

        db.query("""

            UPDATE reagents SET location='{location}' WHERE
            reagent_id={id}

            """.format(location=location, id=id))

def edit_equipment(equipment):
    id = equipment["equipment_id"]
    selection = choose_field(["Name", "Status", "Location"])

    if selection == "Name":
        name = raw_input("Enter a new name: ")

        db.query("""

            UPDATE equipment SET name='{name}' WHERE
            equipment_id={id}

            """.format(name=name, id=id))
    
    elif selection == "Status":
        status = raw_input("Enter new status: ")

        db.query("""

            UPDATE equipment SET status='{status}' WHERE
            equipment_id={id}

            """.format(status=status, id=id))

    elif selection == "Location":
        location = raw_input("Enter new location: ")

        db.query("""

            UPDATE equipment SET location='{location}' WHERE
            equipment_id={id}

            """.format(location=location, id=id))

    
    
