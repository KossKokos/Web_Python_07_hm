
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship 
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE'))
    groups = relationship('Group', backref='students')

    @hybrid_property
    def full_name(self):
        return self.first_name + ' ' + self.last_name


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(20), nullable=False)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    @hybrid_property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    

class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    discipline_name = Column(String(20), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'))
    teachers = relationship('Teacher', backref='disciplines')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    disciplines_id = Column(Integer, ForeignKey('disciplines.id', ondelete='CASCADE'))
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    grade = Column(Integer, nullable=False)
    date_of = Column(Date, nullable=False)
    disciplines = relationship('Discipline', backref='grades')
    students = relationship('Student', backref='grades')
