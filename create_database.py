
# Create tables and fill with initial values

import _mysql

db=_mysql.connect(host="localhost",user="root",
                  passwd="cats123", db="data")

setup = """

DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS experiments;
DROP TABLE IF EXISTS procedures;
DROP TABLE IF EXISTS reagents;
DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS measurments;
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
    value REAL,
    type VARCHAR(30),
    PRIMARY KEY (measurement_id)
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
