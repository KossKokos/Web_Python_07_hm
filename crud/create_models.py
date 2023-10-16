
import random
import sys
sys.path.append('src')

from sqlalchemy import func

from db import session
from models import Student, Teacher, Discipline, Grade, Group

def create_student(first_name: str, last_name: str):
    groups = session.query(func.count(Group.id)).select_from(Group).one()
    student = Student(first_name=first_name,
                      last_name=last_name,
                      group_id = random.randint(1, int(groups[0])))
    session.add(student)
    session.commit()    
    return 'Student was added successfully'

def create_teacher(first_name, last_name):
    teacher = Teacher(first_name=first_name,
                      last_name=last_name)
    session.add(teacher)
    session.commit()
    return 'Teacher was added successfully'

def create_group(name):
    group = Group(group_name=name)
    session.add(group)
    session.commit()
    return 'Group was added successfully'

def create_discipline(name):
    teachers = session.query(func.count(Teacher.id)).select_from(Teacher).one()
    discipline = Discipline(discipline_name=name,
                            teacher_id=random.randint(1, int(teachers[0])))
    session.add(discipline)
    session.commit()
    return 'Discipline was added successfully'

def create_grade(grade, date_of):
    discipline_id = session.query(func.count(Discipline.id)).select_from(Discipline).one()
    students_id = session.query(func.count(Student.id)).select_from(Student).one()
    grade = Grade(grade=grade,
                  disciplines_id=random.randint(1, int(discipline_id[0])),
                  student_id=random.randint(1, int(students_id[0])),
                  date_of=date_of)
    session.add(grade)
    session.commit()
    return 'Grade was added successfully'