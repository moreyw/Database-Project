from database import *
import create
import edit

create = {
    'projects' : create.new_project,
    'procedures' : create.new_procedure,
    'experiments' : create.new_experiment,
    'reagents' : create.new_reagent,
    'equipment' : create.new_equipment,
    'specimens' : create.new_specimen
}

edit = {
    'projects' : edit.edit_project,
    'procedures' : edit.edit_procedure,
    'experiments' : edit.edit_experiment,
    'reagents' : edit.edit_reagent,
    'equipment' : edit.edit_equipment,
    'specimens' : edit.edit_specimen
}
    

def choose_existing(statement):
    db.query(statement)
    r=db.store_result()

    #get all rows as dictionaries
    rows = r.fetch_row(maxrows=0, how=1)
    size = len(rows)

    if not size:
        return None
    
    for num, row in enumerate(rows):
        print "{}: {}".format(num, row["name"])

    choice = None
    while choice not in range(size):
        try:
            choice = int(raw_input("Select an existing value: "))
            if choice not in range(size):
                raise ValueError("invalid choice")
                
        except Exception:
            print "Invalid choice, please try again."

    return rows[choice]

def create_new(value_type):
    return create[value_type]()

def make_choice(name, statement, new_option=True):
    choice = None
    if new_option:
        while choice not in range(1, 3):
            try:
                choice = int(raw_input("Choose existing {}[1] or create new[2]: ".format(name)))
                if choice not in range(1, 3):
                    raise ValueError("invalid choice")
                    
            except Exception:
                print "Invalid choice, please try again."
    else:
        choice = 1

    if choice == 1:
        selected = choose_existing(statement)
        if selected:
            return selected
        else:
            print "No existing " + name + ". Creating new item."
            choice = 2

    if choice == 2:
        return create_new(name)
