
import sys
sys.path.append("src")
from db import session
from models import Student, Teacher, Group, Grade, Discipline

def list_student():
    result = session.query(Student).all()
    for mod in result:
        print(mod.id, mod.full_name, mod.groups.group_name)

def list_teacher():
    result = session.query(Teacher).all()
    for mod in result:
        print(mod.id, mod.full_name)

def list_group():
    result = session.query(Group).all()
    for mod in result:
        print(mod.id, mod.group_name)

def list_discipline():
    result = session.query(Discipline).all()
    for mod in result:
        print(mod.id, mod.discipline_name, mod.teacher_id, mod.teachers.full_name)

def list_grade():
    result = session.query(Grade).all()
    for mod in result:
        print(mod.id, mod.disciplines.discipline_name , mod.students.full_name, mod.grade, mod.date_of)
