from app import db

from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import backref, relationship



class Department(db.Model):

    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    misc = db.Column(JSON)


class Role(db.Model):

    __tablename__ = 'roles'
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())


class Employee(db.Model):

    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = db.Column(db.DateTime, default=datetime.now())
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    department = relationship(
        Department,
        backref=backref('employees',
                        uselist=True,
                        cascade='delete,all'))
    role = relationship(
        Role,
        backref=backref('roles',
                        uselist=True,
                        cascade='delete,all'))

