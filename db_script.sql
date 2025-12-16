-- Contact Book Table
CREATE TABLE contacts (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name VARCHAR2(100) NOT NULL,
    phone_number VARCHAR2(15) NOT NULL,
    created_date DATE DEFAULT SYSDATE
);

-- Check if table created
SELECT * FROM contacts;