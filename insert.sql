/* TROOP */
INSERT INTO troop (troop_name, troop_address, troop_website, troop_telephone_number)
VALUES ("troop0", "Address from troop 0", "website.url@troop0.com", "000000000");

INSERT INTO troop (troop_name, troop_address, troop_website, troop_telephone_number)
VALUES ("troop1", "Address from troop 1", "website.url@troop1.com", "111111111");

INSERT INTO troop (troop_name, troop_address, troop_website, troop_telephone_number)
VALUES ("troop2", "Address from troop 2", "website.url@troop2.com", "222222222");

INSERT INTO troop (troop_name, troop_address, troop_website, troop_telephone_number)
VALUES ("troop3", "Address from troop 3", "website.url@troop3.com", "333333333");

INSERT INTO troop (troop_name, troop_address, troop_website, troop_telephone_number)
VALUES ("troop4", "Address from troop 4", "website.url@troop4.com", "444444444");

/* SECTION TYPE */
INSERT INTO section_type (code, descr)
VALUES ("Junior", "This section type is specialized in age groups from 6 to 8 years");

INSERT INTO section_type (code, descr)
VALUES ("Pre-teen", "This section type is specialized in age groups from 9 to 11 years");

INSERT INTO section_type (code, descr)
VALUES ("Teen", "This section type is specialized in age groups from 12 to 14 years");

INSERT INTO section_type (code, descr)
VALUES ("Adolescent", "This section type is specialized in age groups from 15 to 17 years");

/* NATIONAL EVENTS */
INSERT INTO national_events (event_id, event_name, detailed_info, event_start_date, event_end_date, event_location, event_cost, aplication_closing_date)
VALUES ("0", "Event0", "This event is intended to learn the meaning of number 0", "2019-1-10", "2019-1-20", "CORK city hall", "0", "2019-1-01");

INSERT INTO national_events (event_id, event_name, detailed_info, event_start_date, event_end_date, event_location, event_cost, aplication_closing_date)
VALUES ("1", "Event1", "This event is intended to learn the meaning of number 1", "2019-1-10", "2019-1-20", "CORK city hall", "10", "2019-1-01");

INSERT INTO national_events (event_id, event_name, detailed_info, event_start_date, event_end_date, event_location, event_cost, aplication_closing_date)
VALUES ("2", "Event2", "This event is intended to learn the meaning of number 2", "2019-1-10", "2019-1-20", "CORK city hall", "20", "2019-1-01");

INSERT INTO national_events (event_id, event_name, detailed_info, event_start_date, event_end_date, event_location, event_cost, aplication_closing_date)
VALUES ("3", "Event3", "This event is intended to learn the meaning of number 3", "2019-1-10", "2019-1-20", "CORK city hall", "30", "2019-1-01");

INSERT INTO national_events (event_id, event_name, detailed_info, event_start_date, event_end_date, event_location, event_cost, aplication_closing_date)
VALUES ("4", "Event4", "This event is intended to learn the meaning of number 4", "2019-1-10", "2019-1-20", "CORK city hall", "40", "2019-1-01");

/* MEMBER ATTENDS EVENT */
INSERT INTO member_attends_event (member_id, event_id)
VALUES ("member0", "0");

INSERT INTO member_attends_event (member_id, event_id)
VALUES ("member1", "1");

INSERT INTO member_attends_event (member_id, event_id)
VALUES ("member2", "2");

INSERT INTO member_attends_event (member_id, event_id)
VALUES ("member3", "3");

INSERT INTO member_attends_event (member_id, event_id)
VALUES ("member4", "4");

/* EVENT IS ORGANIZED FOR SECTION TYPE */

INSERT INTO event_is_organized_for_section_type (section_type_code, event_id)
VALUES ("Junior", "0");

INSERT INTO event_is_organized_for_section_type (section_type_code, event_id)
VALUES ("Junior", "1");

INSERT INTO event_is_organized_for_section_type (section_type_code, event_id)
VALUES ("Pre-teen", "2");

INSERT INTO event_is_organized_for_section_type (section_type_code, event_id)
VALUES ("Teen", "3");

INSERT INTO event_is_organized_for_section_type (section_type_code, event_id)
VALUES ("Adolescent", "4");


/* VOLUNTEER */

/* SECTION */

/* MEMBER */

