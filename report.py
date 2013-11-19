from database import *

def measurement_report(measurement):
    print("  Type: {}, Value: {}".format(measurement["type"],
                                         measurement["value"]))
    

def specimen_report(specimen):
    print("  Specimen Name: {}".format(specimen["name"]))
    print("  Specimen Origin: {}".format(specimen["origin"]))

    print("  Specimen Measurements:")

    db.query("""
    
    SELECT * FROM measurements WHERE
    specimen_id={}
    
    """.format(specimen["specimen_id"]))

    r=db.store_result()

    #get all rows as dictionaries
    rows = r.fetch_row(maxrows=0, how=1)

    if len(rows) == 0:
        print("  None")
        return
        
    for measurement in rows:
        measurement_report(measurement)
    

def equipment_report(equipment):
    print("  Equipment Name: {}".format(equipment["name"]))
    print("  Equipment Status: {}".format(equipment["status"]))
    print("  Equipment Location: {}".format(equipment["location"]))

def reagent_report(reagent):
    print("  Reagent Name: {}".format(reagent["name"]))
    print("  Reagent Status: {}".format(reagent["status"]))
    print("  Reagent Location: {}".format(reagent["location"]))


def procedure_report(procedure):
    print("  Procedure Name: {}".format(procedure["name"]))
    print("  Procedure Description: {}".format(procedure["description"]))

    print("Reagents used: ")

    db.query("""
    
    SELECT * FROM use_reagents, reagents WHERE
    procedure_id={}
    
    """.format(procedure["procedure_id"]))

    r=db.store_result()

    #get all rows as dictionaries
    rows = r.fetch_row(maxrows=0, how=1)

    if len(rows) == 0:
        print("  None")
        return
        
    for reagent in rows:
        reagent_report(reagent)

    print("Equipment used: ")
    
    db.query("""
    
    SELECT * FROM use_equipment, equipment WHERE
    procedure_id={}
    
    """.format(procedure["procedure_id"]))

    r=db.store_result()

    #get all rows as dictionaries
    rows = r.fetch_row(maxrows=0, how=1)

    if len(rows) == 0:
        print("  None")
        return
        
    for reagent in rows:
        equipment_report(reagent)
    

def experiment_report(experiment):
    print("  Experiment Name: {}".format(experiment["name"]))

    db.query("""
    
    SELECT * FROM procedures WHERE
    procedure_id={}
    
    """.format(experiment["procedure_id"]))

    r=db.store_result()

    #get all rows as dictionaries
    rows = r.fetch_row(maxrows=0, how=1)

    procedure_report(rows[0])

    print("Specimens used:")

    db.query("""
    
    SELECT * FROM specimens, use_specimens WHERE
    experiment_id={}
    
    """.format(experiment["experiment_id"]))

    r=db.store_result()

    #get all rows as dictionaries
    rows = r.fetch_row(maxrows=0, how=1)
    if len(rows) == 0:
        print("  None")
        return
    for specimen in rows:
        specimen_report(specimen)
        

def project_report(project):
    
    print("Project Name: {}".format(project["name"]))

    db.query("""
    
    SELECT * FROM experiments WHERE
    experiments.project_id={}
    
    """.format(project["project_id"]))

    r=db.store_result()

    #get all rows as dictionaries
    rows = r.fetch_row(maxrows=0, how=1)

    print("Project experiments:")
    if len(rows) == 0:
        print("  None")
        
    for experiment in rows:
        experiment_report(experiment)
        
    print("")


def generate_report(to_file=False):

    db.query("""
    
    SELECT * FROM projects
    
    """)

    r=db.store_result()

    #get all rows as dictionaries
    rows = r.fetch_row(maxrows=0, how=1)

    for project in rows:
        project_report(project)
