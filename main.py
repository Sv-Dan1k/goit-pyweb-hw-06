import sqlite3
from faker import Faker
import random
from datetime import datetime


conn = sqlite3.connect('university.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY,
    name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY,
    name TEXT,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
)
''')


fake = Faker()


groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cursor.execute('INSERT INTO groups (name) VALUES (?)', (group,))


teachers = [fake.name() for _ in range(4)]
for teacher in teachers:
    cursor.execute('INSERT INTO teachers (name) VALUES (?)', (teacher,))


subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']
for subject in subjects:
    teacher_id = random.choice(range(1, 5))
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (subject, teacher_id))


for _ in range(30):
    name = fake.name()
    group_id = random.choice(range(1, 4))
    cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (name, group_id))


for student_id in range(1, 31):
    for subject_id in range(1, 6):
        for _ in range(20):
            grade = random.randint(1, 100)
            date = fake.date_this_year()
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', 
                           (student_id, subject_id, grade, date))

conn.commit()
conn.close()

