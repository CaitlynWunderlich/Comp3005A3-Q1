# Comp3005A3-Q1

## Setup the Database:
1. Open PgAdmin and create a database titled university
2. Create a new query and run the following to create the students table
```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);
```
3. Populate the table using the following query
```sql
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```

## Execute the Program
1. Install psycopg2 using pip install psycopg2
2. Change user and student values in comp3005a3.py to match your postgresql details
3. Run the program and follow the prompts in the terminal to VIEW, ADD, UPDATE, and DELETE users from the students table
