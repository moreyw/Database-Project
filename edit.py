
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
    selection = choose_field(["Name", "Description", "Equipment", "Reagents"])
    
    
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

    elif selection == "Equipment":
        equipment, option = choice.relation_choice("equipment", """
                SELECT e.name, e.equipment_id FROM 
                    procedures p, equipment e, use_equipment u WHERE
                    p.procedure_id = u.procedure_id AND 
                    e.equipment_id = u.equipment_id
                """)
        if option == "add":
            db.query("""

                INSERT INTO use_equipment (equipment_id, procedure_id)
                VALUES ('{}', '{}') 

            """.format(equipment["equipment_id"], procedure["procedure_id"]))
        elif option == "remove" and equipment:
            db.query("""

                DELETE FROM use_equipment WHERE equipment_id={} AND procedure_id={}

                """.format(equipment["equipment_id"], procedure["procedure_id"]))

    elif selection == "Reagents":
        reagent, option = choice.relation_choice("reagents", """
                        SELECT r.name, r.reagent_id FROM 
                            reagents r, procedures p, use_reagents u WHERE
                            p.procedure_id = u.procedure_id AND
                            r.reagent_id = u.reagent_id
                        """)
        if option == "add":
            print "Here"
            db.query("""

                INSERT INTO use_reagents (reagent_id, procedure_id)
                VALUES ('{}', '{}') 

            """.format(reagent["reagent_id"], procedure["procedure_id"]))
        elif option == "remove" and reagent:
            db.query("""

                DELETE FROM use_reagents WHERE reagent_id={} AND procedure_id={}

                """.format(reagent["reagent_id"], procedure["procedure_id"]))
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
    db.commit()

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
    db.commit()

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
    db.commit()

def edit_specimen(specimen):
    id = specimen["specimen_id"]
    selection = choose_field(["Name", "Origin", "Measurements"])

    if selection=="Name":
        name = raw_input("Enter a new name: ")

        db.query("""

            UPDATE specimens SET name='{name}' WHERE
            specimen_id={id}

            """.format(name=name, id=id))

    elif selection=="Origin":
        origin = raw_input("Enter a new origin: ")

        db.query("""

            UPDATE specimens SET origin='{origin}' WHERE
            specimen_id={id}

            """.format (origin=origin, id=id))

    elif selection=="Measurements":
        return
    db.commit()
    
