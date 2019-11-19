CREATE TABLE IF NOT EXISTS troop(
    troop_name VARCHAR(50) PRIMARY KEY,
    troop_address VARCHAR (50) NOT NULL,
    troop_website VARCHAR (50) UNIQUE,
    troop_telephone_number VARCHAR (12) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS section_type(
    code VARCHAR(50) PRIMARY KEY,
    descr VARCHAR (100) NOT NULL
);

CREATE TABLE IF NOT EXISTS national_events(
    event_id VARCHAR(50) PRIMARY KEY,
    event_name VARCHAR (15) UNIQUE NOT NULL,
    detailed_info VARCHAR (200) NOT NULL,
    event_start_date DATE NOT NULL ,
    event_end_date DATE NOT NULL ,
    event_location VARCHAR (25) NOT NULL,
    event_cost INTEGER NOT NULL,
    aplication_closing_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS member_attends_event(
    member_id VARCHAR(50),
    event_id VARCHAR(50),
    PRIMARY KEY (member_id, event_id)
);

CREATE TABLE IF NOT EXISTS event_is_organized_for_section_type(
    section_type_code VARCHAR(50),
    event_id VARCHAR(50),
    PRIMARY KEY (section_type_code, event_id)
);


CREATE TABLE IF NOT EXISTS volunteer(
    volunteer_id VARCHAR(50) PRIMARY KEY,
    volunteer_name VARCHAR (15) NOT NULL,
    volunteer_address VARCHAR (25) NOT NULL,
    volunteer_phone_number VARCHAR (12) NOT NULL,
    date_of_birth DATE,
    volunteer_gender VARCHAR (15),
    vetting_completion_date DATE NOT NULL,
    troop_name VARCHAR(50),
    FOREIGN KEY (troop_name) REFERENCES troop(troop_name)
);


CREATE TABLE IF NOT EXISTS section(
    section_name VARCHAR(50) PRIMARY KEY,
    section_type VARCHAR (15) NOT NULL,
    meeting_day VARCHAR (15) NOT NULL,
    meeting_start_time VARCHAR (15) NOT NULL,
    meeting_end_time VARCHAR (15) NOT NULL   ,
    volunteer_id VARCHAR(50),
    FOREIGN KEY (volunteer_id) REFERENCES volunteer(volunteer_id),
    troop_name VARCHAR(50),
    FOREIGN KEY (troop_name) REFERENCES troop(troop_name),
    FOREIGN KEY (section_type) REFERENCES section_type(code)
);

CREATE TABLE IF NOT EXISTS member(
    member_id VARCHAR(50) PRIMARY KEY,
    member_name VARCHAR (15) NOT NULL,
    member_address VARCHAR (25) NOT NULL,
    date_of_birth DATE NOT NULL,
    member_gender VARCHAR (15),
    parent_guardian VARCHAR (15) NOT NULL,
    parent_guardian_phone_number VARCHAR (12) NOT NULL,
    section_name VARCHAR(50),
    FOREIGN KEY (section_name) REFERENCES section(section_name)
);