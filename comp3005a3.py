
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="localhost",
    database="university",
    user="postgres",
    password="student"
)

#display student table
def getAllStudents():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER by student_id ")
    students = cur.fetchall()

    for student in students:
        print(student)

    conn.commit()
    cur.close()

#add student to student table
def addStudent(first_name, last_name, email, enrollment_date):
    cur = conn.cursor()
    try:
        #check for valid date
        datetime.strptime(enrollment_date, "%Y-%m-%d")

        cur.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES('{first_name}','{last_name}','{email}','{enrollment_date}');")
        print(f"{first_name} {last_name} added as student")

    except Exception as e:
        print("cannot add student")
        print(e)

    finally:
        conn.commit()
        cur.close()

#update student email in student table
def updateStudentEmail(student_id, new_email):
    cur = conn.cursor()
    try:
        cur.execute(f"UPDATE students SET email = '{new_email}' WHERE student_id = {student_id};")
        print("email changed\n")

    except Exception as e:
        print("email cannot be changed")
        print(e)

    finally:
        conn.commit()
        cur.close()

#delete student from student table
def deleteStudent(student_id):
    cur = conn.cursor()
    try:
        cur.execute(f"""DELETE from students WHERE student_id = {student_id}""")
        print("student deleted\n")

    except Exception as e:
        print("student cannot be deleted")
        print(e)

    finally:
        conn.commit()
        cur.close()


def main():

    while(True):
        print("---------------------------------")
        print("-Enter 0 to quit")
        print("-Enter 1 to display student table")
        print("-Enter 2 to add student")
        print("-Enter 3 to update student email")
        print("-Enter 4 to delete student")
        choice = int(input("Your choice: "))

        print("\n")

        if (choice == 0):
            break

        elif (choice == 1):
            getAllStudents()

        elif (choice == 2):
            first = input("Enter student first name: ")
            last = input("Enter student last name: ")
            email = input("Enter student email: ")
            date = input("Enter enrollment date (yyyy-mm-dd): ")
            addStudent(first, last, email, date)

        elif (choice == 3):
            id = input("Enter student id: ")
            email = input("Enter new email: ")
            updateStudentEmail(id, email)

        elif (choice == 4):
            id = input("Enter the id of the student you wish to delete: ")
            deleteStudent(id)


main()
