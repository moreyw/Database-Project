#!/usr/bin/env python

# Create tables and fill with initial values

import _mysql

with open("config.conf", 'r') as file:
    host, user, passwd, db = file.read().split()
    
db=_mysql.connect(host=host,user=user,
                  passwd=passwd, db=db)

setup = """

DROP TABLE IF EXISTS used_on;
DROP TABLE IF EXISTS measurements;
DROP TABLE IF EXISTS use_specimens;
DROP TABLE IF EXISTS specimens;
DROP TABLE IF EXISTS use_equipment;
DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS use_reagents;
DROP TABLE IF EXISTS reagents;
DROP TABLE IF EXISTS experiments;
DROP TABLE IF EXISTS procedures;
DROP TABLE IF EXISTS projects;



CREATE TABLE projects(
    project_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    PRIMARY KEY (project_id)
);

CREATE TABLE procedures(
    procedure_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    description VARCHAR(1000),
    PRIMARY KEY (procedure_id)
);

CREATE TABLE experiments(
    experiment_id INT NOT NULL AUTO_INCREMENT,
    project_id INT NOT NULL,
    procedure_id INT NOT NULL,
    name VARCHAR(100),
    PRIMARY KEY (experiment_id),
    FOREIGN KEY (project_id) REFERENCES projects (project_id) ON DELETE CASCADE,
    FOREIGN KEY (procedure_id) REFERENCES procedures (procedure_id) ON DELETE CASCADE
);

CREATE TABLE reagents(
    reagent_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    status VARCHAR(100), 
    location VARCHAR(100),
    PRIMARY KEY (reagent_id)
);

CREATE TABLE use_reagents(
    procedure_id INT NOT NULL,
    reagent_id INT NOT NULL,
    PRIMARY KEY (reagent_id, procedure_id),
    FOREIGN KEY (reagent_id) REFERENCES reagents (reagent_id) ON DELETE CASCADE,
    FOREIGN KEY (procedure_id) REFERENCES procedures (procedure_id) ON DELETE CASCADE
);

CREATE TABLE equipment(
    equipment_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    status VARCHAR(100), 
    location VARCHAR(100),
    PRIMARY KEY (equipment_id)
);

CREATE TABLE use_equipment(
    equipment_id INT NOT NULL,
    procedure_id INT NOT NULL,
    PRIMARY KEY (equipment_id, procedure_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment (equipment_id) ON DELETE CASCADE,
    FOREIGN KEY (procedure_id) REFERENCES procedures (procedure_id) ON DELETE CASCADE
);

CREATE TABLE specimens(
    specimen_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    origin VARCHAR(100),
    PRIMARY KEY (specimen_id)
);

CREATE TABLE use_specimens(
    specimen_id INT NOT NULL,
    experiment_id INT NOT NULL,
    PRIMARY KEY (specimen_id, experiment_id),
    FOREIGN KEY (specimen_id) REFERENCES specimens (specimen_id) ON DELETE CASCADE,
    FOREIGN KEY (experiment_id) REFERENCES experiments (experiment_id) ON DELETE CASCADE
);

CREATE TABLE measurements(
    measurement_id INT NOT NULL AUTO_INCREMENT,
    specimen_id INT NOT NULL,
    value REAL,
    type VARCHAR(30),
    PRIMARY KEY (measurement_id),
    FOREIGN KEY (specimen_id) REFERENCES specimens (specimen_id) ON DELETE CASCADE
);

CREATE TABLE used_on(
    specimen_id INT NOT NULL,
    procedure_id INT NOT NULL,
    PRIMARY KEY (specimen_id, procedure_id),
    FOREIGN KEY (specimen_id) REFERENCES specimens (specimen_id) ON DELETE CASCADE,
    FOREIGN KEY (procedure_id) REFERENCES procedures (procedure_id) ON DELETE CASCADE
);

#Start inserting test values
INSERT INTO projects (project_id, name) VALUES (NULL, 'Sample Project');

INSERT INTO procedures (procedure_id, name, description) VALUES
    (NULL, 'Sample Procedure', 'Description of Sample Procedure');

INSERT INTO experiments (experiment_id, project_id, procedure_id, name) VALUES
    (NULL, 1, 1, 'New Experiment');

INSERT INTO reagents (reagent_id, name, status, location) VALUES
    (NULL, 'Test Reagent', 'Volatile', 'Fridge');

INSERT INTO use_reagents (procedure_id, reagent_id) VALUES
    (1, 1);

INSERT INTO equipment (equipment_id, name, status, location) VALUES
    (NULL, 'Syringe', 'Contaminated', 'Biohazard container');

INSERT INTO use_equipment(equipment_id, procedure_id) VALUES
    (1, 1);

INSERT INTO specimens (specimen_id, name, origin) VALUES
    (NULL, "Test Specimen", "Sample origin");

INSERT INTO use_specimens (specimen_id, experiment_id) VALUES
    (1, 1);

INSERT INTO measurements (measurement_id, specimen_id, value, type) VALUES
    (NULL, 1, 20, 'Feet');

INSERT INTO used_on (specimen_id, procedure_id) VALUES
    (1, 1);
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


