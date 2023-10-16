import argparse
from datetime import datetime
import sys
sys.path.append('crud')

from create_models import create_student, create_teacher, create_group, create_discipline, create_grade
from update_models import update_student, update_teacher, update_group, update_discipline, update_grade
from remove_models import remove_student, remove_teacher, remove_group, remove_discipline, remove_grade
from list_models import list_student, list_teacher, list_group, list_discipline, list_grade

parser = argparse.ArgumentParser(description='Todo APP')
parser.add_argument('-a', '--action', help='Command: create, update, list, remove')
parser.add_argument('-m', '--model', help='Command: choose table')
parser.add_argument('-n', '--name', help='Name for the model')
parser.add_argument('-id', help='Id of the model')
parser.add_argument('-fn', '--first_name', help='First name for the Student or Teacher')
parser.add_argument('-ln', '--last_name', help='Last name for the Student or Teacher')
parser.add_argument('-gr', '--grade', help='Grade(1-12) for the model Grade')
parser.add_argument('-dt', '--date', help='Date in format dd/mm/yyyy')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
model = my_arg.get('model')
name = my_arg.get('name')
id_ = my_arg.get('id')
first_name = my_arg.get('first_name')
last_name = my_arg.get('last_name')
grade = my_arg.get('grade')
date_of = my_arg.get('date')

create_model = {'Student': create_student,
                 'Teacher': create_teacher, 
                 'Group': create_group, 'Discipline': create_discipline,
                 'Grade': create_grade}

update_model = {'Student': update_student,
                 'Teacher': update_teacher, 
                 'Group': update_group, 'Discipline': update_discipline,
                 'Grade': update_grade}

remove_model = {'Student': remove_student,
                 'Teacher': remove_teacher, 
                 'Group': remove_group, 'Discipline': remove_discipline,
                 'Grade': remove_grade}

list_model = {'Student': list_student,
              'Teacher': list_teacher, 
              'Group': list_group, 'Discipline': list_discipline,
              'Grade': list_grade}

def parse_date(date_):
    day_m_y = date_.split('/')
    datetime_obj = datetime(day=int(day_m_y[0]), month=int(day_m_y[1]), year=int(day_m_y[2]))
    return datetime_obj

def create_action():
    match model:
        case 'Student':
            new_student = create_model.get(model)(first_name, last_name)
            print(new_student)
        case 'Teacher':
            new_teacher = create_model.get(model)(first_name, last_name)
            print(new_teacher)
        case 'Group':
            new_group = create_model.get(model)(name)
            print(new_group)
        case 'Discipline':
            new_discipline = create_model.get(model)(name)
            print(new_discipline)
        case 'Grade':
            day = parse_date(date_of)
            new_grade = create_model.get(model)(grade, day)
            print(new_grade)
        case _:
            print('Wrong params')

def update_action():
    match model:
        case 'Student':
            upd_student = update_model.get(model)(id_, first_name, last_name)
            print(upd_student)
        case 'Teacher':
            upd_student = update_model.get(model)(id_, first_name, last_name)
            print(upd_student)
        case 'Group':
            upd_group = update_model.get(model)(id_, name)
            print(upd_group)
        case 'Discipline':
            upd_discipline = update_model.get(model)(id_, name)
            print(upd_discipline)
        case 'Grade':
            upd_grade = update_model.get(model)(id_, grade)
            print(upd_grade)
        case _:
            print('Wrong params')

def remove_action():
    match model:
        case 'Student':
            rem_student = remove_model.get(model)(id_)
            print(rem_student)
        case 'Teacher':
            rem_teacher = remove_model.get(model)(id_)
            print(rem_teacher)
        case 'Discipline':
            rem_discipline = remove_model.get(model)(id_)
            print(rem_discipline)
        case 'Group':
            rem_group = remove_model.get(model)(id_)
            print(rem_group)
        case 'Grade':
            rem_grade = remove_model.get(model)(id_)
            print(rem_grade)
        case _:
            print('Wrong params')

def list_action():
    try:
        list_model.get(model)()
    except (KeyError, TypeError):
        print('Choose one of these models: (Teacher, Student, Discipline, Group, Grade)')       

def main():
    match action:
        case 'create':
            create_action()
        case 'update':
            update_action()
        case 'remove':
            remove_action()
        case 'list':
            list_action()
        case _:
            print('Wrong params')

if __name__ == '__main__':
    main()
