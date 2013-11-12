
# Create tables and fill with initial values

import _mysql

with open("config.conf", 'r') as file:
    host, user, passwd, db = file.read().split()
    
db=_mysql.connect(host=host,user=user,
                  passwd=passwd, db=db)

setup = """

DROP TABLE IF EXISTS project_experiments;
DROP TABLE IF EXISTS measurements;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS experiments;
DROP TABLE IF EXISTS procedures;
DROP TABLE IF EXISTS reagents;
DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS specimens;


CREATE TABLE projects(
    project_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    PRIMARY KEY (project_id)
);

CREATE TABLE experiments(
    experiment_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    PRIMARY KEY (experiment_id)
);

CREATE TABLE procedures(
    procedure_id INT NOT NULL AUTO_INCREMENT,
    description VARCHAR(1000),
    PRIMARY KEY (procedure_id)
);

CREATE TABLE reagents(
    reagent_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    status VARCHAR(100), 
    location VARCHAR(100),
    PRIMARY KEY (reagent_id)
);

CREATE TABLE equipment(
    equipment_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    status VARCHAR(100), 
    location VARCHAR(100),
    PRIMARY KEY (equipment_id)
);

CREATE TABLE specimens(
    specimen_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    origin VARCHAR(100),
    PRIMARY KEY (specimen_id)
);

CREATE TABLE measurements(
    measurement_id INT NOT NULL AUTO_INCREMENT,
    specimen_id INT NOT NULL,
    value REAL,
    type VARCHAR(30),
    PRIMARY KEY (measurement_id),
    FOREIGN KEY (specimen_id) REFERENCES specimens (specimen_id) ON DELETE CASCADE
);

#Map a project to its experiments
CREATE TABLE project_experiments(
    project_id INT NOT NULL,
    experiment_id INT NOT NULL,
    PRIMARY KEY (project_id, experiment_id),
    FOREIGN KEY (project_id) REFERENCES projects (project_id) ON DELETE CASCADE,
    FOREIGN KEY (experiment_id) REFERENCES experiments (experiment_id) ON DELETE CASCADE
);


"""

#Execute every query in the setup
for query_string in setup.split(";"):
    if query_string.strip():
        print("\nExecuting: ")
        print(query_string.strip())
        db.query(query_string)

#Complete any pending transactions
db.commit()
db.close()

print("\nSetup completed")
