from sqlalchemy import select, func, desc, and_
import sys
sys.path.append("src")
from db import session
from models import Student, Teacher, Group, Grade, Discipline


def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

    result = session.query(Student.full_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result

def select_2():
    # Знайти студента із найвищим середнім балом з певного предмета.

    result = session.query(Student.full_name, Discipline.discipline_name, func.round(func.avg(Grade.grade), 2)\
             .label('avg_grade')).select_from(Grade).join(Student).join(Discipline)\
             .group_by(Student.id, Discipline.discipline_name)\
             .order_by(desc('avg_grade')).limit(1).one()
    return result

def select_3(d_id):
    # Знайти середній бал у групах з певного предмета.

    result = session.query(Group.group_name, Discipline.discipline_name, func.round(func.avg(Grade.grade), 2)\
             .label('avg_grade')).select_from(Grade).join(Student).join(Group).join(Discipline)\
             .filter(Discipline.id == d_id).group_by(Group.group_name, Discipline.discipline_name)\
             .order_by(desc('avg_grade')).all()
    return result

def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).

    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
            .select_from(Grade).one()
    return result

def select_5(t_id):
    # Знайти які курси читає певний викладач.

    result = session.query(Teacher.full_name, Discipline.discipline_name).select_from(Teacher).join(Discipline)\
            .filter(Teacher.id == t_id).group_by(Discipline.id, Teacher.full_name)\
            .order_by(Discipline.discipline_name).all()
    return result

def select_6(gr_id):
    # Знайти список студентів у певній групі.

    result = session.query(Group.group_name, Student.full_name).select_from(Group).join(Student)\
            .filter(Group.id == gr_id).group_by(Group.group_name, Student.full_name).order_by(Student.full_name).all()
    return result

def select_7(gr_id, d_id):
    # Знайти оцінки студентів у окремій групі з певного предмета.
    
    result = session.query(Group.group_name, Discipline.discipline_name, Student.full_name, Grade.grade)\
            .select_from(Grade).join(Discipline).join(Student).join(Group)\
            .filter(and_(Group.id == gr_id, Discipline.id == d_id))\
            .group_by(Group.group_name, Discipline.discipline_name, Student.full_name, Grade.grade)\
            .order_by(desc(Grade.grade)).all()
    return result

def select_8(t_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.

    result = session.query(Teacher.full_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
            .select_from(Grade).join(Discipline).join(Teacher).filter(Teacher.id == t_id)\
            .group_by(Teacher.full_name).order_by(desc('avg_grade')).all()
    return result

def select_9(s_id):
    # Знайти список курсів, які відвідує певний студент.

    result = session.query(Student.full_name, Discipline.discipline_name).select_from(Grade).join(Student)\
            .join(Discipline).filter(Student.id == s_id).group_by(Discipline.discipline_name, Student.full_name)\
            .order_by(Discipline.discipline_name).all()
    return result

def select_10(s_id, t_id):
    # Список курсів, які певному студенту читає певний викладач.

    result = session.query(Student.full_name, Teacher.full_name, Discipline.discipline_name).select_from(Grade)\
            .join(Discipline).join(Student).join(Teacher).filter(and_(Student.id == s_id, Teacher.id == t_id))\
            .group_by(Discipline.discipline_name, Student.full_name, Teacher.full_name)\
            .order_by(Discipline.discipline_name).all()
    return result

def select_11(s_id, t_id):
    # Середній бал, який певний викладач ставить певному студентові.

    result = session.query(Teacher.full_name, Student.full_name, func.round(func.avg(Grade.grade), 2)\
            .label('avg_grade'))\
            .select_from(Grade).join(Discipline).join(Teacher).join(Student)\
            .filter(and_(Student.id == s_id, Teacher.id == t_id))\
            .group_by(Teacher.full_name, Student.full_name).order_by(desc('avg_grade')).all()
    return result

def select_12(d_id, g_id):
    # Оцінки студентів у певній групі з певного предмета на останньому занятті.

    subquery = (select(Grade.date_of).join(Student).join(Group).where(
        and_(Grade.disciplines_id == d_id, Group.id == g_id)).group_by(Grade.date_of)\
        .order_by(desc(Grade.date_of)).limit(1).scalar_subquery())

    result = session.query(Discipline.discipline_name, Student.full_name, Group.group_name, Grade.date_of, Grade.grade)\
        .select_from(Grade).join(Student).join(Discipline).join(Group)\
        .filter(and_(Discipline.id == d_id, Group.id == g_id, Grade.date_of == subquery))\
        .group_by(Student.full_name, Discipline.discipline_name, Group.group_name, Grade.date_of, Grade.grade)\
        .order_by(desc(Grade.grade)).all()
    return result

if __name__ == '__main__':
    print(select_1())
    # print(select_2())
    # print(select_3(5))
    # print(select_4())
    # print(select_5(5))
    # print(select_6(1))
    # print(select_7(1, 2))
    # print(select_8(4))
    # print(select_9(50))
    # print(select_10(3, 1))
    # print(select_11(4, 1))
    # print(select_12(1, 1))