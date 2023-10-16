import sys
sys.path.append('src')

from db import session
from models import Student, Teacher, Discipline, Grade, Group

def update_student(id_, first_name, last_name):
    session.query(Student).filter(Student.id == id_)\
    .update({'first_name': first_name, 'last_name': last_name})
    session.commit()
    return 'Student was updated successfully'

def update_teacher(id_, first_name, last_name):
    session.query(Teacher).filter(Teacher.id == id_)\
    .update({'first_name': first_name, 'last_name': last_name})
    session.commit()
    return 'Teacher was updated successfully'

def update_group(id_, gr_name):
    session.query(Group).filter(Group.id == id_)\
    .update({'group_name': gr_name})
    session.commit()
    return 'Group was updated successfully'

def update_discipline(id_, d_name):
    session.query(Discipline).filter(Discipline.id == id_)\
    .update({'discipline_name': d_name})
    session.commit()
    return 'Discipline was updated successfully'

def update_grade(id_, grade):
    session.query(Grade).filter(Grade.id == id_)\
    .update({'grade': grade})
    session.commit()
    return 'Grade was updated successfully'