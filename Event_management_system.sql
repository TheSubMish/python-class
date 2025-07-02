-- DROP TABLES
BEGIN FOR t IN (
  SELECT table_name FROM user_tables 
  WHERE table_name IN ('BOOKINGLOG','EVENTBOOKINGS','EVENTS','VENUES','PARTICIPANTS')
) LOOP
  EXECUTE IMMEDIATE 'DROP TABLE ' || t.table_name;
END LOOP; END;
/

-- DROP TYPES
BEGIN FOR t IN (
  SELECT type_name FROM user_types 
  WHERE type_name IN (
    'FEEDBACKLIST_T','FEEDBACK_T','SPONSORLIST_T',
    'VIPPARTICIPANT_T','PARTICIPANT_T','CONTACTINFO_T','ADDRESS_T'
  )
) LOOP
  EXECUTE IMMEDIATE 'DROP TYPE ' || t.type_name;
END LOOP; END;
/

-- DROP TRIGGERS
BEGIN FOR trg IN (
  SELECT trigger_name FROM user_triggers 
  WHERE trigger_name IN ('TRG_LIMIT_PARTICIPANTS','TRG_BOOKING_LOG')
) LOOP
  EXECUTE IMMEDIATE 'DROP TRIGGER ' || trg.trigger_name;
END LOOP; END;
/

-- DROP PROCEDURES
BEGIN FOR p IN (
  SELECT object_name FROM user_procedures 
  WHERE object_type = 'PROCEDURE' 
    AND object_name IN ('ADD_PARTICIPANT','ADD_VIP_PARTICIPANT')
) LOOP
  EXECUTE IMMEDIATE 'DROP PROCEDURE ' || p.object_name;
END LOOP; END;
/

-- DROP SEQUENCE
BEGIN
  EXECUTE IMMEDIATE 'DROP SEQUENCE SEQ_BOOKING_LOG';
EXCEPTION WHEN OTHERS THEN NULL;
END;
/

-- OBJECT TYPES
CREATE OR REPLACE TYPE Address_t AS OBJECT (
  street VARCHAR2(100),
  city VARCHAR2(50),
  zip_code VARCHAR2(10)
);
/

CREATE OR REPLACE TYPE ContactInfo_t AS OBJECT (
  phone VARCHAR2(15),
  email VARCHAR2(100)
);
/

-- INHERITANCE TYPES
CREATE OR REPLACE TYPE Participant_t AS OBJECT (
  participant_id NUMBER,
  full_name VARCHAR2(100),
  contact_info ContactInfo_t,
  address Address_t
) NOT FINAL;
/

CREATE OR REPLACE TYPE VIPParticipant_t UNDER Participant_t (
  vip_level VARCHAR2(20)
);
/

-- VARRAY TYPE
CREATE OR REPLACE TYPE SponsorList_t AS VARRAY(5) OF VARCHAR2(100);
/

-- NESTED TABLE TYPE
CREATE OR REPLACE TYPE Feedback_t AS OBJECT (
  participant_id NUMBER,
  comment_text VARCHAR2(300),
  comment_date DATE
);
/



CREATE OR REPLACE TYPE FeedbackList_t AS TABLE OF Feedback_t;
/

-- TABLES
CREATE TABLE Participants OF Participant_t (
  PRIMARY KEY (participant_id)
)
OBJECT IDENTIFIER IS PRIMARY KEY;
/

CREATE TABLE Venues (
  venue_id NUMBER PRIMARY KEY,
  name VARCHAR2(100) NOT NULL,
  address Address_t
);
/






CREATE TABLE Events (
  event_id NUMBER PRIMARY KEY,
  title VARCHAR2(200) NOT NULL,
  event_date DATE,
  venue_id NUMBER REFERENCES Venues(venue_id),
  max_participants NUMBER,
  feedback FeedbackList_t
)
NESTED TABLE feedback STORE AS Feedback_Storage;
/



CREATE TABLE EventBookings (
  booking_id NUMBER PRIMARY KEY,
  participant_id NUMBER REFERENCES Participants(participant_id),
  event_id NUMBER REFERENCES Events(event_id),
  booking_date DATE DEFAULT SYSDATE,
  UNIQUE (participant_id, event_id)
);
/



-- SAMPLE DATA
INSERT INTO Participants VALUES (
  1,
  'Alice Johnson',
  ContactInfo_t('9876543210', 'alice@example.com'),
  Address_t('123 Lane', 'Kathmandu', '44600')
);
INSERT INTO Participants VALUES (
  2,
  'Bob Thapa',
  ContactInfo_t('9812345678', 'bob@example.com'),
  Address_t('456 Avenue', 'Pokhara', '33700')
);

INSERT INTO Participants VALUES (
  3,
  'Rita Lama',
  ContactInfo_t('9801010101', 'rita@example.com'),
  Address_t('Sundhara', 'Kathmandu', '44600')
);

INSERT INTO Participants VALUES (
  4,
  'Sita Gurung',
  ContactInfo_t('9802020202', 'sita@example.com'),
  Address_t('Chipledhunga', 'Pokhara', '33700')
);
INSERT INTO Participants VALUES(
  5,
  'Void gaming',
  ContactInfo_t('9811874212', 'voidgaming@gmail.com'),
  Address_t('Bharatpur-8', 'Chitwan', '44201')
);  

-- VIP participant
INSERT INTO Participants VALUES (
  VIPParticipant_t(6, 'Diamond VIP', ContactInfo_t('9800000000', 'vip@example.com'), Address_t('VIP Rd', 'Lalitpur', '44700'), 'Gold')
);
INSERT INTO Participants VALUES (
  VIPParticipant_t(7,'Luffy', ContactInfo_t('9812345678', 'luffy@gmail.com'), Address_t('East Blue', 'One Piece_Japan', '12312'), 'Diamond')
);




INSERT INTO Venues VALUES (1, 'City Hall', Address_t('Main Street', 'Kathmandu', '44600'));
INSERT INTO Venues VALUES (2, 'Lakeside Arena', Address_t('Lakeside Rd', 'Pokhara', '33700'));

INSERT INTO Events VALUES (
  101, 'Tech Conference 2025', TO_DATE('2025-09-10', 'YYYY-MM-DD'), 1, 100,
  FeedbackList_t()
);

INSERT INTO Events VALUES (
  102, 'Music Festival', TO_DATE('2025-10-15', 'YYYY-MM-DD'), 2, 200,
  FeedbackList_t()
);

INSERT INTO EventBookings VALUES (1, 1, 101, SYSDATE);
INSERT INTO EventBookings VALUES (2, 2, 102, SYSDATE);
INSERT INTO EventBookings VALUES (3, 3, 101, SYSDATE);
INSERT INTO EventBookings VALUES (4, 4, 102, SYSDATE);
INSERT INTO EventBookings VALUES (5, 5, 101, SYSDATE);




-- TRIGGER: Prevent Overbooking
CREATE OR REPLACE TRIGGER trg_limit_participants
BEFORE INSERT ON EventBookings
FOR EACH ROW
DECLARE
  cnt NUMBER;
  max_cap NUMBER;
BEGIN
  SELECT COUNT(*) INTO cnt FROM EventBookings WHERE event_id = :NEW.event_id;
  SELECT max_participants INTO max_cap FROM Events WHERE event_id = :NEW.event_id;
  IF cnt >= max_cap THEN
    RAISE_APPLICATION_ERROR(-20001, 'Maximum participants reached for this event.');
  END IF;
END;
/



-- Procedure 1: Add new participant
CREATE OR REPLACE PROCEDURE add_participant(
    p_id IN NUMBER,
    p_name IN VARCHAR2,
    p_phone IN VARCHAR2,
    p_email IN VARCHAR2,
    p_street IN VARCHAR2,
    p_city IN VARCHAR2,
    p_zip IN VARCHAR2
)
IS
BEGIN
    INSERT INTO Participants VALUES (
        p_id,
        p_name,
        ContactInfo_t(p_phone, p_email),
        Address_t(p_street, p_city, p_zip)
    );
    DBMS_OUTPUT.PUT_LINE('Participant ' || p_name || ' added successfully with ID: ' || p_id);
    COMMIT;
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
        DBMS_OUTPUT.PUT_LINE('Error: Participant with ID ' || p_id || ' already exists');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error adding participant: ' || SQLERRM);
        ROLLBACK;
END;
/



BEGIN
    DBMS_OUTPUT.PUT_LINE('=== ADDING NEW PARTICIPANTS ===');
    add_participant(8, 'John Doe', '9876543210', 'john@example.com', '789 Street', 'Kathmandu', '44600');
    add_participant(9, 'Jane Smith', '9812345678', 'jane@example.com', '321 Road', 'Pokhara', '33700');
END;
/


-- Procedure 2: Add VIP participant
CREATE OR REPLACE PROCEDURE add_vip_participant(
    p_id IN NUMBER,
    p_name IN VARCHAR2,
    p_phone IN VARCHAR2,
    p_email IN VARCHAR2,
    p_street IN VARCHAR2,
    p_city IN VARCHAR2,
    p_zip IN VARCHAR2,
    p_vip_level IN VARCHAR2
)
IS
BEGIN
    INSERT INTO Participants VALUES (
        VIPParticipant_t(
            p_id, p_name, 
            ContactInfo_t(p_phone, p_email),
            Address_t(p_street, p_city, p_zip),
            p_vip_level
        )
    );
    DBMS_OUTPUT.PUT_LINE('VIP Participant ' || p_name || ' (' || p_vip_level || ') added successfully');
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error adding VIP participant: ' || SQLERRM);
        ROLLBACK;
END;
/

-- TESTING VIP PARTICIPANT PROCEDURE
-- Call the add_vip_participant procedure with test data
BEGIN
    DBMS_OUTPUT.PUT_LINE('=== TESTING ADD_VIP_PARTICIPANT PROCEDURE ===');
    DBMS_OUTPUT.PUT_LINE('Adding VIP participants...');
    DBMS_OUTPUT.PUT_LINE('');
    
    -- Add first VIP participant
    add_vip_participant(
        p_id => 20,
        p_name => 'Sarah Williams',
        p_phone => '9876543210',
        p_email => 'sarah@vip.com',
        p_street => '123 VIP Boulevard',
        p_city => 'Kathmandu',
        p_zip => '44600',
        p_vip_level => 'Platinum'
    ); 
    -- Add second VIP participant
    add_vip_participant(
        p_id => 21,
        p_name => 'Michael Johnson',
        p_phone => '9812345678',
        p_email => 'michael@elite.com',
        p_street => '456 Elite Street',
        p_city => 'Pokhara',
        p_zip => '33700',
        p_vip_level => 'Diamond'
    );   
    -- Add third VIP participant
    add_vip_participant(
        p_id => 22,
        p_name => 'Emma Davis',
        p_phone => '9801234567',
        p_email => 'emma@gold.com',
        p_street => '789 Gold Avenue',
        p_city => 'Lalitpur',
        p_zip => '44700',
        p_vip_level => 'Gold'
    );
    DBMS_OUTPUT.PUT_LINE('');
    DBMS_OUTPUT.PUT_LINE('=== VIP PARTICIPANTS ADDED SUCCESSFULLY ===');
END;
/
-- Query to display all VIP participants that were just added
PROMPT === DISPLAYING ALL VIP PARTICIPANTS ===
SELECT 
    p.participant_id,
    p.full_name,
    p.contact_info.phone AS phone,
    p.contact_info.email AS email,
    p.address.street AS street,
    p.address.city AS city,
    p.address.zip_code AS zip_code,
    TREAT(VALUE(p) AS VIPParticipant_t).vip_level AS vip_level,
    'VIP' AS participant_type
FROM Participants p
WHERE VALUE(p) IS OF (VIPParticipant_t)
ORDER BY p.participant_id;



-- 2. TESTING PARTICIPANT COUNT FUNCTION
-- First, let's add some bookings to test the function
BEGIN
    DBMS_OUTPUT.PUT_LINE('');
    DBMS_OUTPUT.PUT_LINE('=== ADDING BOOKINGS FOR TESTING ===');
    
    -- Book some events for our new VIP participants
    INSERT INTO EventBookings VALUES (10, 20, 101, SYSDATE); -- Sarah books Tech Conference
    INSERT INTO EventBookings VALUES (11, 21, 101, SYSDATE); -- Michael books Tech Conference  
    INSERT INTO EventBookings VALUES (12, 22, 102, SYSDATE); -- Emma books Music Festival
    INSERT INTO EventBookings VALUES (13, 20, 102, SYSDATE); -- Sarah also books Music Festival
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Bookings added successfully!');
END;
/
-- Now test the get_participant_count function
BEGIN
    DBMS_OUTPUT.PUT_LINE('');
    DBMS_OUTPUT.PUT_LINE('=== TESTING GET_PARTICIPANT_COUNT FUNCTION ===');
    DBMS_OUTPUT.PUT_LINE('');
    -- Test for Event 101 (Tech Conference)
    DBMS_OUTPUT.PUT_LINE('Event 101 (Tech Conference) - Participant Count: ' || get_participant_count(101)); 
    -- Test for Event 102 (Music Festival)
    DBMS_OUTPUT.PUT_LINE('Event 102 (Music Festival) - Participant Count: ' || get_participant_count(102));
    
    -- Test for non-existent event
    DBMS_OUTPUT.PUT_LINE('Event 999 (Non-existent) - Participant Count: ' || get_participant_count(999));
    
    DBMS_OUTPUT.PUT_LINE('');
    DBMS_OUTPUT.PUT_LINE('Note: -1 indicates error or non-existent event');
END;
/




-- Query to show event details with participant counts
PROMPT
PROMPT === EVENT DETAILS WITH PARTICIPANT COUNTS ===
SELECT 
    e.event_id,
    e.title,
    TO_CHAR(e.event_date, 'DD-MON-YYYY') AS event_date,
    v.name AS venue_name,
    e.max_participants,
    get_participant_count(e.event_id) AS current_participants,
    (e.max_participants - get_participant_count(e.event_id)) AS available_spots,
    ROUND((get_participant_count(e.event_id) / e.max_participants) * 100, 2) AS occupancy_percentage
FROM Events e
JOIN Venues v ON e.venue_id = v.venue_id
ORDER BY e.event_id;





-- Log booking activity
CREATE TABLE BookingLog (
    log_id NUMBER PRIMARY KEY,
    participant_id NUMBER,
    event_id NUMBER,
    action VARCHAR2(10),
    log_date DATE DEFAULT SYSDATE
);
/

CREATE SEQUENCE seq_booking_log START WITH 1 INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER trg_booking_log
AFTER INSERT OR DELETE ON EventBookings
FOR EACH ROW
BEGIN
    IF INSERTING THEN
        INSERT INTO BookingLog (log_id, participant_id, event_id, action, log_date)
        VALUES (seq_booking_log.NEXTVAL, :NEW.participant_id, :NEW.event_id, 'BOOK', SYSDATE);
    ELSIF DELETING THEN
        INSERT INTO BookingLog (log_id, participant_id, event_id, action, log_date)
        VALUES (seq_booking_log.NEXTVAL, :OLD.participant_id, :OLD.event_id, 'CANCEL', SYSDATE);
    END IF;
END;
/

-- Query A
SELECT 
    eb.booking_id,
    p.participant_id,
    p.full_name,
    e.event_id,
    e.title AS event_title,
    TO_CHAR(e.event_date, 'DD-MON-YYYY') AS event_date,
    v.name AS venue_name,
    v.address.city AS venue_city
FROM EventBookings eb
-- INNER JOIN Participants (every booking must have a participant)
INNER JOIN Participants p ON eb.participant_id = p.participant_id
-- INNER JOIN Events (every booking must belong to an event)
INNER JOIN Events e ON eb.event_id = e.event_id
-- LEFT OUTER JOIN Venues (in case a venue is missing, still show the event)
LEFT OUTER JOIN Venues v ON e.venue_id = v.venue_id
-- CORRECTED: Access nested object attribute properly
WHERE v.address.city = 'Kathmandu'
ORDER BY eb.booking_id;




INSERT INTO TABLE(SELECT feedback FROM Events WHERE event_id = 101)
VALUES (Feedback_t(1, 'Great tech conference! Very informative sessions.', SYSDATE));

INSERT INTO TABLE(SELECT feedback FROM Events WHERE event_id = 101)
VALUES (Feedback_t(3, 'Excellent speakers and networking opportunities.', SYSDATE));

INSERT INTO TABLE(SELECT feedback FROM Events WHERE event_id = 101)
VALUES (Feedback_t(5, 'Amazing event! Well organized and valuable content.', SYSDATE));

INSERT INTO TABLE(SELECT feedback FROM Events WHERE event_id = 102)
VALUES (Feedback_t(2, 'Fantastic music festival! Great atmosphere.', SYSDATE));

INSERT INTO TABLE(SELECT feedback FROM Events WHERE event_id = 102)
VALUES (Feedback_t(4, 'Love the variety of artists and perfect venue.', SYSDATE));

COMMIT;








-- Query B - Event Feedback Analysis
SELECT 
    e.event_id,
    e.title AS event_name,
    TO_CHAR(e.event_date, 'DD-MON-YYYY') AS event_date,
    v.name AS venue_name,
    -- Access nested table elements
    f.participant_id,
    f.comment_text,
    TO_CHAR(f.comment_date, 'DD-MON-YYYY HH24:MI') AS feedback_date,
    -- Determine participant type using sub-type checking
    p.full_name AS participant_name,
    p.contact_info.email AS participant_email,
    CASE 
        WHEN VALUE(p) IS OF (VIPParticipant_t) THEN 
            'VIP - ' || TREAT(VALUE(p) AS VIPParticipant_t).vip_level
        ELSE 
            'Regular'
    END AS participant_status,
    -- Count total feedback for this event using CARDINALITY
    CARDINALITY(e.feedback) AS total_feedback_count
FROM Events e
-- Join with venues
JOIN Venues v ON e.venue_id = v.venue_id
-- Unnest the nested table to access individual feedback records
JOIN TABLE(e.feedback) f ON 1=1  -- Use JOIN instead of comma syntax
-- Join with participants to get participant details
JOIN Participants p ON f.participant_id = p.participant_id
-- Only show events that have feedback
WHERE CARDINALITY(e.feedback) > 0
-- Order by event and feedback date
ORDER BY e.event_id, f.comment_date DESC;




--Query no C

SELECT 
    e.event_id,
    e.title AS event_title,
    f.participant_id,
    p.full_name,
    CASE 
        WHEN VALUE(p) IS OF (VIPParticipant_t) THEN 
            'VIP - ' || TREAT(VALUE(p) AS VIPParticipant_t).vip_level
        ELSE 'Regular'
    END AS participant_status,
    f.comment_text,
    TO_CHAR(f.comment_date, 'DD-MON-YYYY') AS feedback_date,
    s.COLUMN_VALUE AS sponsor
FROM Events e
-- Use of nested table: feedback
CROSS JOIN TABLE(e.feedback) f
JOIN Participants p ON f.participant_id = p.participant_id
JOIN Venues v ON e.venue_id = v.venue_id
-- Use of VARRAY: sponsors
CROSS JOIN TABLE(v.sponsors) s
ORDER BY e.event_id, f.comment_date;


---Query no D
SELECT 
    e.event_id,
    e.title AS event_name,
    e.event_date,
    -- Calculate days until event using interval arithmetic
    (e.event_date - CURRENT_DATE) DAY(9) TO SECOND AS days_until_event,
    -- Temporal analysis of booking patterns
    MIN(eb.booking_date) AS first_booking_date,
    MAX(eb.booking_date) AS last_booking_date,
    -- Calculate booking duration (time between first and last booking)
    (MAX(eb.booking_date) - MIN(eb.booking_date)) DAY(9) TO SECOND AS booking_period,
    -- Temporal aggregation of bookings by week
    COUNT(CASE WHEN eb.booking_date BETWEEN SYSTIMESTAMP - INTERVAL '7' DAY AND SYSTIMESTAMP THEN 1 END) AS bookings_last_7_days,
    COUNT(CASE WHEN eb.booking_date BETWEEN SYSTIMESTAMP - INTERVAL '14' DAY AND SYSTIMESTAMP - INTERVAL '7' DAY THEN 1 END) AS bookings_7_to_14_days_ago,
    -- Calculate average booking time before event
    AVG(e.event_date - eb.booking_date) AS avg_days_booked_in_advance,
    -- Temporal pattern of VIP vs regular bookings
    COUNT(CASE WHEN VALUE(p) IS OF (VIPParticipant_t) THEN 1 END) AS vip_bookings,
    COUNT(CASE WHEN VALUE(p) IS NOT OF (VIPParticipant_t) THEN 1 END) AS regular_bookings
FROM 
    Events e
JOIN 
    EventBookings eb ON e.event_id = eb.event_id
JOIN 
    Participants p ON eb.participant_id = p.participant_id
GROUP BY 
    e.event_id, e.title, e.event_date
ORDER BY 
    days_until_event;
    



    
      
--Query E
SELECT 
    v.address.city AS city,
    TO_CHAR(e.event_date, 'YYYY-Q') AS quarter,
    CASE 
        WHEN VALUE(p) IS OF (VIPParticipant_t) THEN 'VIP' 
        ELSE 'Regular' 
    END AS participant_type,
    COUNT(DISTINCT eb.participant_id) AS participant_count,
    COUNT(DISTINCT e.event_id) AS event_count,
    -- Running total of participants by city
    SUM(COUNT(DISTINCT eb.participant_id)) OVER (
        PARTITION BY v.address.city 
        ORDER BY TO_CHAR(e.event_date, 'YYYY-Q')
    ) AS running_total_participants,
    -- Percentage of total participants by city
    ROUND(COUNT(DISTINCT eb.participant_id) * 100.0 / 
          SUM(COUNT(DISTINCT eb.participant_id)) OVER (PARTITION BY v.address.city), 2) AS percentage_of_city
FROM 
    Events e
JOIN 
    Venues v ON e.venue_id = v.venue_id
JOIN 
    EventBookings eb ON e.event_id = eb.event_id
JOIN 
    Participants p ON eb.participant_id = p.participant_id
GROUP BY 
    ROLLUP(
        v.address.city,
        TO_CHAR(e.event_date, 'YYYY-Q'),
        CASE WHEN VALUE(p) IS OF (VIPParticipant_t) THEN 'VIP' ELSE 'Regular' END
    )
ORDER BY 
    v.address.city NULLS LAST, 
    quarter NULLS LAST, 
    participant_type NULLS LAST;