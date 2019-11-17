CREATE TABLE IF NOT EXISTS troop(
    troop_name VARCHAR(50) PRIMARY KEY,
    troop_address VARCHAR (50) NOT NULL,
    troop_website VARCHAR (50) NOT NULL,
    troop_telephone_number VARCHAR (12) NOT NULL
);

CREATE TABLE IF NOT EXISTS section(
    section_name VARCHAR(50) PRIMARY KEY,
    section_type VARCHAR (50) NOT NULL,
    meeting_day VARCHAR (50) NOT NULL,
    meeting_start_time VARCHAR (12) NOT NULL,
    meeting_end_time VARCHAR (12) NOT NULL   
);

CREATE TABLE IF NOT EXISTS youth_member(
    member_id VARCHAR(50) PRIMARY KEY,
    member_name VARCHAR (50) NOT NULL,
    member_address VARCHAR (50) NOT NULL,
    date_of_birth VARCHAR (20) NOT NULL,
    member_gender VARCHAR (12) NOT NULL ,
    parent_guardian VARCHAR (50) NOT NULL,
    parent_guardian_phone_number VARCHAR (50) NOT NULL
);

CREATE TABLE IF NOT EXISTS adult_volunteer(
    volunteer_id VARCHAR(50) PRIMARY KEY,
    volunteer_name VARCHAR (50) NOT NULL,
    volunteer_address VARCHAR (50) NOT NULL,
    volunteer_phone_number VARCHAR (12) NOT NULL ,
    date_of_birth VARCHAR (20) NOT NULL,
    volunteer_gender VARCHAR (12) NOT NULL ,
    parent_guardian VARCHAR (50) NOT NULL,
    vetted BOOLEAN NOT NULL,
    vetting_completion_date VARCHAR (20) NOT NULL
);

CREATE TABLE IF NOT EXISTS national_events(
    event_id VARCHAR(50) PRIMARY KEY,
    event_name VARCHAR (50) NOT NULL,
    detailed_info VARCHAR (100) NOT NULL,
    event_start_date VARCHAR (20) NOT NULL ,
    event_end_date VARCHAR (20) NOT NULL ,
    event_location VARCHAR (50) NOT NULL,
    event_cost INTEGER NOT NULL,
    vetted BOOLEAN NOT NULL,
    aplication_closing_date VARCHAR (20) NOT NULL
);