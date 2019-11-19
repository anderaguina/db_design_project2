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
INSERT INTO volunteer (volunteer_id, volunteer_name, volunteer_address, volunteer_phone_number, date_of_birth, volunteer_gender, vetting_completion_date, troop_name)
VALUES ("0", "Volunteer0", "Volunteer address 0", "000000000", "1995-1-19", "male", "2015-2-06", "troop0");

INSERT INTO volunteer (volunteer_id, volunteer_name, volunteer_address, volunteer_phone_number, date_of_birth, volunteer_gender, vetting_completion_date, troop_name)
VALUES ("1", "Volunteer1", "Volunteer address 1", "111111111", "1995-1-19", "female", "2015-2-06", "troop1");

INSERT INTO volunteer (volunteer_id, volunteer_name, volunteer_address, volunteer_phone_number, date_of_birth, volunteer_gender, vetting_completion_date, troop_name)
VALUES ("2", "Volunteer2", "Volunteer address 2", "222222222", "1995-1-19", "male", "2015-2-06", "troop2");

INSERT INTO volunteer (volunteer_id, volunteer_name, volunteer_address, volunteer_phone_number, date_of_birth, volunteer_gender, vetting_completion_date, troop_name)
VALUES ("3", "Volunteer3", "Volunteer address 3", "333333333", "1995-1-19", "female", "2015-2-06", "troop3");

INSERT INTO volunteer (volunteer_id, volunteer_name, volunteer_address, volunteer_phone_number, date_of_birth, volunteer_gender, vetting_completion_date, troop_name)
VALUES ("4", "Volunteer4", "Volunteer address 4", "444444444", "1995-1-19", "male", "2015-2-06", "troop4");

/* SECTION */
INSERT INTO section (section_name, section_type, meeting_day, meeting_start_time, meeting_end_time, volunteer_id, troop_name)
VALUES ("section0", "Junior", "0", "17:30", "18:30", "0", "troop0");

INSERT INTO section (section_name, section_type, meeting_day, meeting_start_time, meeting_end_time, volunteer_id, troop_name)
VALUES ("section1", "Junior", "1", "13:30", "14:30", "1", "troop1");

INSERT INTO section (section_name, section_type, meeting_day, meeting_start_time, meeting_end_time, volunteer_id, troop_name)
VALUES ("section2", "Pre-teen", "2", "16:30", "17:30", "2", "troop2");

INSERT INTO section (section_name, section_type, meeting_day, meeting_start_time, meeting_end_time, volunteer_id, troop_name)
VALUES ("section3", "Teen", "3", "19:30", "20:30", "3", "troop3");

INSERT INTO section (section_name, section_type, meeting_day, meeting_start_time, meeting_end_time, volunteer_id, troop_name)
VALUES ("section4", "Adolescent", "4", "21:30", "22:30", "4", "troop4");

/* MEMBER */

INSERT INTO member (member_id, member_name, member_address, date_of_birth, member_gender, parent_guardian, parent_guardian_phone_number, section_name)
VALUES ("0", "Member 0", "Address of member 0", "1995-02-06", "female", "Parent 0", "000000000", "section0");

INSERT INTO member (member_id, member_name, member_address, date_of_birth, member_gender, parent_guardian, parent_guardian_phone_number, section_name)
VALUES ("1", "Member 1", "Address of member 1", "1995-02-06", "male", "Parent 1", "111111111", "section1");

INSERT INTO member (member_id, member_name, member_address, date_of_birth, member_gender, parent_guardian, parent_guardian_phone_number, section_name)
VALUES ("2", "Member 2", "Address of member 2", "1995-02-06", "female", "Parent 2", "222222222", "section2");

INSERT INTO member (member_id, member_name, member_address, date_of_birth, member_gender, parent_guardian, parent_guardian_phone_number, section_name)
VALUES ("3", "Member 3", "Address of member 3", "1995-02-06", "male", "Parent 3", "333333333", "section3");

INSERT INTO member (member_id, member_name, member_address, date_of_birth, member_gender, parent_guardian, parent_guardian_phone_number, section_name)
VALUES ("4", "Member 4", "Address of member 4", "1995-02-06", "female", "Parent 4", "444444444", "section4");

