import sqlite3
from faker import Faker
import random
import datetime

# initialisation of the Faker object
fake = Faker()

# SQLite database connection
conn = sqlite3.connect('university.db')
c = conn.cursor()

# Creation of tables
c.execute('''CREATE TABLE IF NOT EXISTS students (
             student_id INTEGER PRIMARY KEY,
             name TEXT,
             group_id INTEGER)''')

c.execute('''CREATE TABLE IF NOT EXISTS groups (
             group_id INTEGER PRIMARY KEY,
             name TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS teachers (
             teacher_id INTEGER PRIMARY KEY,
             name TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS subjects (
             subject_id INTEGER PRIMARY KEY,
             name TEXT,
             teacher_id INTEGER)''')

c.execute('''CREATE TABLE IF NOT EXISTS grades (
             grade_id INTEGER PRIMARY KEY,
             student_id INTEGER,
             subject_id INTEGER,
             grade INTEGER,
             date TEXT)''')

# Filling the table of students
def populate_students(num_students):
    for _ in range(num_students):
        name = fake.name()
        group_id = random.randint(1, 3)  
        c.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))
        conn.commit()

# Filling the table of groups
def populate_groups():
    groups = ['Group A', 'Group B', 'Group C']
    for name in groups:
        c.execute("INSERT INTO groups (name) VALUES (?)", (name,))
        conn.commit()

# Filling the table of teachers
def populate_teachers(num_teachers):
    for _ in range(num_teachers):
        name = fake.name()
        c.execute("INSERT INTO teachers (name) VALUES (?)", (name,))
        conn.commit()

# Filling the table of subjects
def populate_subjects(num_subjects):
    for _ in range(num_subjects):
        name = fake.word()
        teacher_id = random.randint(1, 3) 
        c.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (name, teacher_id))
        conn.commit()

# Filling the table of grades
def populate_grades(num_grades):
    for _ in range(num_grades):
        student_id = random.randint(1, 30)  
        subject_id = random.randint(1, 8)  
        grade = random.randint(1, 100)  
        date = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')  
        c.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)", (student_id, subject_id, grade, date))
        conn.commit()

# Filling database
populate_groups()
populate_students(30)  # 30 students
populate_teachers(5)  # 5 teachers
populate_subjects(8)  # 8 subjects
populate_grades(600)  # 600 grades

# Close the connection to the database
conn.close()
