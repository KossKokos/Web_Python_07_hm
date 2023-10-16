import sys
sys.path.append('src')

from sqlalchemy import delete
from db import session
from models import Student, Teacher, Discipline, Grade, Group

def remove_student(id_):
    session.query(Student).where(Student.id == id_).delete()
    session.commit()
    return 'Student was removed successfully'

def remove_teacher(id_):
    session.query(Teacher).where(Teacher.id == id_).delete()
    session.commit()
    return 'Teacher was removed successfully'

def remove_group(id_):
    session.query(Group).where(Group.id == id_).delete()
    session.commit()
    return 'Group was removed successfully'

def remove_discipline(id_):
    session.query(Discipline).where(Discipline.id == id_).delete()
    session.commit()
    return 'Discipline was removed successfully'

def remove_grade(id_):
    session.query(Grade).where(Grade.id == id_).delete()
    session.commit()
    return 'Grade was removed successfully'