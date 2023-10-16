import random
from datetime import date, datetime, timedelta
import sys

from faker import Faker
from sqlalchemy import select

sys.path.append("src")
from db import session
from models import Student, Teacher, Group, Grade, Discipline

def main():
    disciplines = [
        'Maths',
        'English',
        'IT',
        'PE',
        'History of Ukraine',
        'Philosophy',
        'Physic',
        'Chemistry'
    ]

    groups = ['C331', 'TP-05-1', 'KN-51']
    NUMBER_TEACHERS = 5
    NUMBER_STUDENTS = 50

    fake = Faker()

    def get_dates(start: date, end: date):
        result = []
        while start <= end:
            if start.isoweekday() < 6:
                result.append(start)
            start += timedelta(days=1)
        return result


    def insert_teachers():
        for _ in range(NUMBER_TEACHERS):
            teacher = Teacher(
                first_name = fake.first_name(),
                last_name=fake.last_name()
            )
            session.add(teacher)
        session.commit()

    def insert_disciplines():
        teachers = session.scalars(select(Teacher.id)).all()
        for discipline in disciplines:
            d = Discipline(
                discipline_name=discipline,
                teacher_id=random.choice(teachers) 
            )
            session.add(d)
        session.commit()

    def insert_groups():
        for group in groups:
            session.add(Group(group_name=group))
        session.commit()

    def insert_students():
        groups_id = session.scalars(select(Group.id)).all()
        for _ in range(NUMBER_STUDENTS):
            student = Student(
                first_name = fake.first_name(),
                last_name=fake.last_name(),
                group_id = random.choice(groups_id)
            )
            session.add(student)
        session.commit()

    def insert_grades():
        start_date = datetime(year=2023, month=9, day=3)
        end_date = datetime(year=2024, month=6, day=15)
        studying_dates = get_dates(start=start_date, end=end_date)

        students_id = session.scalars(select(Student.id)).all()
        disciplines_id = session.scalars(select(Discipline.id)).all()

        for day in studying_dates:
            students = [random.choice(students_id) for _ in range(5)]
            for student in students:
                gr = Grade(
                    disciplines_id = random.choice(disciplines_id),
                    student_id = student,
                    grade = random.randint(1, 12),
                    date_of = day
                )
                session.add(gr)
        session.commit()

    insert_teachers()
    insert_disciplines()
    insert_groups()
    insert_students()
    insert_grades()

if __name__ == '__main__':
    main()
